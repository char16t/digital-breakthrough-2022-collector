#!/usr/bin/env python3

import os
import re
import numpy as np
import pandas as pd
import torch
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk
import h2o
from h2o.estimators import H2OKMeansEstimator
from lightautoml.automl.presets.tabular_presets import TabularAutoML
from lightautoml.tasks import Task
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

nltk.download('punkt')

N_THREADS = 1
RANDOM_STATE = 42
ISSUES_SUMMARY_FIELD = "summary"
ISSUES_TARGET = "overall_worklogs"
ISSUES_SUMMARY_D2V_MODEL_PATH = "target/summary.d2v.model"
COMMENTS_TEXT_D2V_MODEL_PATH = "target/comments.d2v.model"
ISSUES_TRAIN_PATH = "data/train_issues.csv"
COMMENT_TRAIN_PATH = "data/train_comments.csv"
EMPLOYEES_PATH = "data/employees.csv"
ISSUES_TEST = "data/test_issues.csv"
COMMENT_TEST = "data//test_comments.csv"

# Reproducibility

np.random.seed(RANDOM_STATE)
#torch.set_num_threads(N_THREADS)
h2o.init(nthreads=N_THREADS)

# Read original data

df_issues_train = pd.read_csv(ISSUES_TRAIN_PATH)
df_comment_train = pd.read_csv(COMMENT_TRAIN_PATH)
df_emp = pd.read_csv(EMPLOYEES_PATH)
df_issues_test = pd.read_csv(ISSUES_TEST)
df_comment_test = pd.read_csv(COMMENT_TEST)

# Merge train and test parts of ISSUES datasets
df_issues_train_without_overall_worklogs = \
  df_issues_train.loc[:, df_issues_train.columns!=ISSUES_TARGET]
df_issues_all = pd.concat([df_issues_train_without_overall_worklogs, df_issues_test])

# Merge train and test parts of COMMENTS datasets
df_comment_all = pd.concat([df_comment_train, df_comment_test])

def is_exists(fpath):
  if os.path.isfile(fpath): return True
  else: return False

def build_d2v(input_texts, output_path, **params):
  tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(input_texts)]
  max_epochs = params.get('max_epochs', 100)
  vec_size = params.get('vec_size', 20)
  alpha = params.get('alpha', 0.025)
  model = Doc2Vec(vector_size=vec_size,
                  alpha=alpha, 
                  min_alpha=0.00025,
                  min_count=1,
                  dm=0)
  model.build_vocab(tagged_data)
  for epoch in range(max_epochs):
      print('{1}: iteration {0}'.format(epoch, output_path))
      model.train(tagged_data,
                  total_examples=model.corpus_count,
                  epochs=model.epochs)
      # decrease the learning rate
      model.alpha -= 0.0002
      # fix the learning rate, no decay
      model.min_alpha = model.alpha
      model.save(output_path)

def to_vec(text, model, **params):
  alpha = params.get('alpha', 0.1)
  min_alpha = params.get('min_alpha', 0.0001)
  steps = params.get('steps', 50)
  def prepare_text(text):
    replace = {
      r'\[\~.*?\]': r"X_MENTION",
      r'!.*?!': r"X_SCREENSHOT",
      r'{quote}.*?{quote}': r"X_QUOTE",
      r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*': r"X_LINK",
      r'\[(.*?)\|.*?\]': r"\1"
    }
    s = text
    for k, v in replace.items():
      s = re.sub(k, v, s)
    return s
  def cast_vector(row):
    r = np.array(list(map(lambda x: x.astype('double'), row)))
    return r
  test_data = word_tokenize(prepare_text(text.lower()))
  return cast_vector(model.infer_vector(test_data, alpha=alpha, 
                                        min_alpha=min_alpha,steps=steps))

def cluster_vecs(vecs_all, vecs_train, vecs_test, **params):
  k = params.get('k', 100)
  vecs_train_h2o = h2o.H2OFrame(vecs_train)
  vecs_test_h2o = h2o.H2OFrame(vecs_test)
  kmeans = H2OKMeansEstimator(k=k,
                              estimate_k=False,
                              standardize=False,
                              seed=RANDOM_STATE)
  kmeans.train(x=vecs_all.columns.to_numpy().tolist(),
                    training_frame=vecs_train_h2o,
                    validation_frame=vecs_test_h2o)
  vcs_h2o = h2o.H2OFrame(vecs_all)
  return kmeans.predict(vcs_h2o).as_data_frame()

def cluster_by_clustered_count(dataframe, col1, col2, col1_unique, col2_unique, **params):
  k = params.get('k', 100)
  gr = dataframe.groupby([col1, col2])[col2].count()
  counts = gr.reset_index(name='count')
  def count_col1_col2(col1_value, col2_value):
    res = counts[(counts[col1] == col1_value) & (counts[col2] == col2_value)]
    if res.shape[0] > 0:
      return res.iloc[0]['count']
    else:
      return 0  
  matrix = []
  for col1_unique_value in col1_unique:
    row = []
    for col2_unique_value in col2_unique:
      row.append(count_col1_col2(col1_unique_value, col2_unique_value))
    matrix.append(row)
  pass
  df = pd.DataFrame(data=np.array(matrix))
  df_train, df_test = train_test_split(df, test_size=0.25, shuffle=False, random_state=RANDOM_STATE)
  # df_train = df.sample(frac = 0.75)
  # df_test = df.drop(df_train.index)
  df_clustered = pd.DataFrame(data=[[x] for x in col1_unique], columns=[col1])
  df_clustered[col2] = cluster_vecs(df, df_train, df_test, k=k)
  return df_clustered

def smart_fill_na(dataframe, id_field, known_fields, target_field):
  df = dataframe[[id_field] + known_fields + [target_field]]
  
  df_test = df[df[target_field].isnull()]
  df_test = df_test[df_test.columns[1:-1]]

  if df_test.shape[0] == 0:
    return dataframe

  from supervised.automl import AutoML
  automl = AutoML(eval_metric="accuracy", ml_task="multiclass_classification", random_state=RANDOM_STATE)
  X_train = df[df[target_field].notnull()]
  X_train = X_train[X_train.columns[1:-1]]
  y_train = df[df[target_field].notnull()][target_field]
  automl.fit(X_train, y_train)
  y_pred = automl.predict(df_test)

  res = df[df[target_field].isnull()]
  res = res[[id_field]]
  res['pred'] = y_pred
  res
  def get_empty_field(emp_id):
    r = res[res[id_field] == emp_id]
    if r.shape[0] > 0:
      return r.iloc[0]['pred']
    else:
      return ''
  df_restored = dataframe
  df_restored[target_field] = df_restored.apply(lambda row: get_empty_field(row[id_field]) if pd.isnull(row[target_field]) else row[target_field], axis=1)
  return df_restored

def encode_caterorical_feature(dataframe, column_name):
  from sklearn.preprocessing import OneHotEncoder
  enc = OneHotEncoder(handle_unknown='ignore')
  X = dataframe[[column_name]]
  enc.fit(X)
  position_encoded = pd.DataFrame(data=enc.transform(X).toarray(), columns=[column_name + "_" + str(v) for i,v in enumerate(enc.categories_[0])])
  #enc.categories_
  result = pd.concat([dataframe, position_encoded], axis=1).drop([column_name], axis = 1)
  return result

# Clustering issues by summary
if not is_exists(ISSUES_SUMMARY_D2V_MODEL_PATH):
  build_d2v(df_issues_all[ISSUES_SUMMARY_FIELD], ISSUES_SUMMARY_D2V_MODEL_PATH, 
            max_epochs=100, vec_size=20, alpha=0.025)
issues_d2v_summary_model = Doc2Vec.load(ISSUES_SUMMARY_D2V_MODEL_PATH)

summary_vecs_data = df_issues_all.apply(lambda row: to_vec(row[ISSUES_SUMMARY_FIELD], issues_d2v_summary_model, alpha=0.025, min_alpha=0.0001, steps=100), axis=1)
summary_vecs_all = pd.DataFrame(data=[vec for vec in summary_vecs_data]).add_prefix("summary_vec_")
summary_vecs_train = summary_vecs_all.iloc[:df_issues_train.shape[0],:]
summary_vecs_test = summary_vecs_all.iloc[df_issues_train.shape[0]:,:]

summary_cluster_all = cluster_vecs(summary_vecs_all, summary_vecs_train, summary_vecs_test, k=100)
summary_cluster_train = summary_cluster_all.iloc[:df_issues_train.shape[0],:]
summary_cluster_test = summary_cluster_all.iloc[df_issues_train.shape[0]:,:]

# Clustering comments by text
if not is_exists(COMMENTS_TEXT_D2V_MODEL_PATH):
  build_d2v(df_comment_all['text'], COMMENTS_TEXT_D2V_MODEL_PATH, 
            max_epochs=100, vec_size=20, alpha=0.025)
comment_d2v_text_model = Doc2Vec.load(COMMENTS_TEXT_D2V_MODEL_PATH)

comment_vecs_data = df_comment_all.apply(lambda row: to_vec(row['text'], comment_d2v_text_model, alpha=0.025, min_alpha=0.0001, steps=100), axis=1)
comment_vecs_all = pd.DataFrame(data=[vec for vec in comment_vecs_data]).add_prefix("comment_vec_")
comment_vecs_train = comment_vecs_all.iloc[:df_comment_train.shape[0],:]
comment_vecs_test = comment_vecs_all.iloc[df_comment_train.shape[0]:,:]

comment_cluster_all = cluster_vecs(comment_vecs_all, comment_vecs_train, comment_vecs_test, k=100)
comment_cluster_train = summary_cluster_all.iloc[:df_issues_train.shape[0],:]
comment_cluster_test = summary_cluster_all.iloc[df_issues_train.shape[0]:,:]

# Cluster employees
users_comments_clusters_data = df_comment_all[['author_id']]
users_comments_clusters_data['cluster'] = comment_cluster_all.values
clusters = comment_cluster_all['predict'].unique()
users = df_emp['id'].unique()
user_comments_cluster = cluster_by_clustered_count(users_comments_clusters_data, 'author_id', 'cluster', users, clusters, k=100)

users_issues_assignee_data = df_issues_all[['assignee_id']]
users_issues_assignee_data['cluster'] = summary_cluster_all.values
clusters = summary_cluster_all['predict'].unique()
users = df_emp['id'].unique()
issue_assignee_cluster = cluster_by_clustered_count(users_issues_assignee_data, 'assignee_id', 'cluster', users, clusters, k=100)

users_issues_cretor_data = df_issues_all[['creator_id']]
users_issues_cretor_data['cluster'] = summary_cluster_all.values
clusters = summary_cluster_all['predict'].unique()
users = df_emp['id'].unique()
issue_creator_cluster = cluster_by_clustered_count(users_issues_cretor_data, 'creator_id', 'cluster', users, clusters, k=100)

employee_cluster = pd.DataFrame()
employee_cluster['id'] = users
employee_cluster['comments_cluster'] = user_comments_cluster['cluster'].values
employee_cluster['assignee_cluster'] = issue_assignee_cluster['cluster'].values
employee_cluster['creator_cluster'] = issue_creator_cluster['cluster'].values

employee_cluster_train_tmp, employee_cluster_test_tmp = train_test_split(employee_cluster, test_size=0.25, shuffle=False, random_state=RANDOM_STATE)
employee_cluster_result = pd.DataFrame()
employee_cluster_result['id'] = employee_cluster['id']
employee_cluster_result['cluster'] = cluster_vecs(employee_cluster, employee_cluster_train_tmp, employee_cluster_test_tmp, k=100)
employee_cluster_result

# Cluster issues by comments
issues_comments_data = df_comment_all[['issue_id']]
issues_comments_data['cluster'] = comment_cluster_all.values
clusters = comment_cluster_all['predict'].unique()
issues = df_comment_all['issue_id'].unique()
issue_comments_cluster = cluster_by_clustered_count(issues_comments_data, 'issue_id', 'cluster', issues, clusters, k=100)

# Restore empty fields of employees
df_emp2 = df_emp
df_emp2['comments_cluster'] = user_comments_cluster['cluster'].values
df_emp2['assignee_cluster'] = issue_assignee_cluster['cluster'].values
df_emp2['creator_cluster'] = issue_creator_cluster['cluster'].values
#df['position'] = df_emp['position']
employees = smart_fill_na(df_emp2, 'id', 
    ['is_nda_signed', 'is_labor_contract_signed', 'is_added_to_internal_chats', 
     'is_added_one_to_one', 'comments_cluster', 'assignee_cluster', 
     'creator_cluster'], 
     'position')
employees = smart_fill_na(employees, 'id', 
    ['is_nda_signed', 'is_labor_contract_signed', 'is_added_to_internal_chats', 
     'is_added_one_to_one', 'comments_cluster', 'assignee_cluster', 
     'creator_cluster', 'position'], 
     'hiring_type')
employees = smart_fill_na(employees, 'id', 
    ['is_nda_signed', 'is_labor_contract_signed', 'is_added_to_internal_chats', 
     'is_added_one_to_one', 'comments_cluster', 'assignee_cluster', 
     'creator_cluster', 'position', 'hiring_type'], 
     'payment_type')
employees = smart_fill_na(employees, 'id', 
    ['is_nda_signed', 'is_labor_contract_signed', 'is_added_to_internal_chats', 
     'is_added_one_to_one', 'comments_cluster', 'assignee_cluster', 
     'creator_cluster', 'position', 'hiring_type', 'payment_type'], 
     'salary_calculation_type')
employees = smart_fill_na(employees, 'id', 
    ['is_nda_signed', 'is_labor_contract_signed', 'is_added_to_internal_chats', 
     'is_added_one_to_one', 'comments_cluster', 'assignee_cluster', 
     'creator_cluster', 'position', 'hiring_type', 'payment_type', 'salary_calculation_type'], 
     'english_level')
employees = employees.drop(["active","full_name", "salary_calculation_type", "passport", 'is_nda_signed', 'is_labor_contract_signed', 'is_added_to_internal_chats', 
     'is_added_one_to_one', 'payment_type', 'salary_calculation_type'], axis = 1)
#employees = encode_caterorical_feature(employees, 'position')
employees = encode_caterorical_feature(employees, 'hiring_type')
#employees = encode_caterorical_feature(employees, 'payment_type')
#employees = encode_caterorical_feature(employees, 'salary_calculation_type')

english_le = LabelEncoder()
english_le.fit(['A1', 'A2', 'B1', 'B2', 'C1'])
english_le.transform(['A1'])[0]
employees['english_level'] = employees.apply(lambda row: english_le.transform([row['english_level']])[0], axis=1)

employees_prefixed_a = employees[['id', 'assignee_cluster', 'comments_cluster', 'position']].add_prefix("assignee_")
employees_prefixed_c = employees[['id', 'creator_cluster', 'comments_cluster', 'position']].add_prefix("creator_")
issues_merged = pd.merge(df_issues_all, employees_prefixed_a, left_on="assignee_id", right_on="assignee_id", how='inner')
issues_merged = pd.merge(issues_merged, employees_prefixed_c, left_on="creator_id", right_on="creator_id", how='inner')
issues_merged = issues_merged.drop(['id', 'key', 'created', 'summary'], axis=1)

issues_merged_train = issues_merged.iloc[:df_issues_train.shape[0],:]
issues_merged_test = issues_merged.iloc[df_issues_train.shape[0]:,:]

df_result_train = issues_merged_train
df_result_train['summary_cluster'] = summary_cluster_train.values
#df_result_train['assignee_cluster'] = df_issues_train.apply(lambda row: employee_cluster_result[employee_cluster_result['id'] == row['assignee_id']].iloc[0]['cluster'], axis=1)
#df_result_train['creator_cluster'] = df_issues_train.apply(lambda row: employee_cluster_result[employee_cluster_result['id'] == row['creator_id']].iloc[0]['cluster'], axis=1)

#df_result_train['assignee_comments_cluster'] = df_issues_train.apply(lambda row: employee_cluster[employee_cluster['id'] == row['assignee_id']].iloc[0]['comments_cluster'], axis=1)
#df_result_train['assignee_assignee_cluster'] = df_issues_train.apply(lambda row: employee_cluster[employee_cluster['id'] == row['assignee_id']].iloc[0]['assignee_cluster'], axis=1)
#df_result_train['assignee_creator_cluster'] = df_issues_train.apply(lambda row: employee_cluster[employee_cluster['id'] == row['assignee_id']].iloc[0]['creator_cluster'], axis=1)

#df_result_train['creator_comments_cluster'] = df_issues_train.apply(lambda row: employee_cluster[employee_cluster['id'] == row['creator_id']].iloc[0]['comments_cluster'], axis=1)
#df_result_train['creator_assignee_cluster'] = df_issues_train.apply(lambda row: employee_cluster[employee_cluster['id'] == row['creator_id']].iloc[0]['assignee_cluster'], axis=1)
#df_result_train['creator_creator_cluster'] = df_issues_train.apply(lambda row: employee_cluster[employee_cluster['id'] == row['creator_id']].iloc[0]['creator_cluster'], axis=1)

df_result_train = df_result_train.drop(['creator_id', 'assignee_id'], axis=1)

def get_comments_cluster(issue_id):
  res = issue_comments_cluster[issue_comments_cluster['issue_id'] == issue_id]
  if res.shape[0] > 0:
    return res.iloc[0]['cluster']
  else:
    return -1
df_result_train['comments_cluster'] = df_issues_train.apply(lambda row: get_comments_cluster(row['id']), axis=1)
df_result_train[ISSUES_TARGET] = df_issues_train[ISSUES_TARGET]

automl = TabularAutoML(
    task = Task('reg', metric = lambda y_true, y_pred: r2_score(y_true, y_pred)), 
    reader_params = {'random_state': RANDOM_STATE},
)
oof_pred = automl.fit_predict(df_result_train,  roles = {'target': ISSUES_TARGET})
#df_result_train

df_result_test = issues_merged_test
df_result_test['summary_cluster'] = summary_cluster_test.values
#df_result_test['assignee_cluster'] = df_issues_test.apply(lambda row: employee_cluster_result[employee_cluster_result['id'] == row['assignee_id']].iloc[0]['cluster'], axis=1)
#df_result_test['creator_cluster'] = df_issues_test.apply(lambda row: employee_cluster_result[employee_cluster_result['id'] == row['creator_id']].iloc[0]['cluster'], axis=1)

# df_result_test['assignee_comments_cluster'] = df_issues_test.apply(lambda row: employee_cluster[employee_cluster['id'] == row['assignee_id']].iloc[0]['comments_cluster'], axis=1)
# df_result_test['assignee_assignee_cluster'] = df_issues_test.apply(lambda row: employee_cluster[employee_cluster['id'] == row['assignee_id']].iloc[0]['assignee_cluster'], axis=1)
# df_result_test['assignee_creator_cluster'] = df_issues_test.apply(lambda row: employee_cluster[employee_cluster['id'] == row['assignee_id']].iloc[0]['creator_cluster'], axis=1)
# df_result_test['creator_comments_cluster'] = df_issues_test.apply(lambda row: employee_cluster[employee_cluster['id'] == row['creator_id']].iloc[0]['comments_cluster'], axis=1)
# df_result_test['creator_assignee_cluster'] = df_issues_test.apply(lambda row: employee_cluster[employee_cluster['id'] == row['creator_id']].iloc[0]['assignee_cluster'], axis=1)
# df_result_test['creator_creator_cluster'] = df_issues_test.apply(lambda row: employee_cluster[employee_cluster['id'] == row['creator_id']].iloc[0]['creator_cluster'], axis=1)
df_result_test['comments_cluster'] = df_issues_test.apply(lambda row: get_comments_cluster(row['id']), axis=1)
df_result_test = df_result_test.drop(['creator_id', 'assignee_id'], axis=1)

#df_result_test[ISSUES_TARGET] = df_issues_train[ISSUES_TARGET]

test_pred = automl.predict(df_result_test).data
test_pred = [np.floor(row[0]).astype(np.int64) for row in test_pred]

df_result = pd.DataFrame()
df_result["id"] = df_issues_test["id"]
df_result[ISSUES_TARGET] = test_pred
df_result.to_csv('solution.csv', index=False)
df_result

from supervised.automl import AutoML
automl = AutoML(mode="Explain", explain_level=2, eval_metric="r2", ml_task="regression", random_state=RANDOM_STATE)
X_train = df_result_train[df_result_train.columns[:-1]]
y_train = df_result_train[ISSUES_TARGET]
automl.fit(X_train, y_train)
y_pred = automl.predict(df_result_test)
y_pred = [np.floor(x).astype(np.int64) for x in y_pred]

df_result = pd.DataFrame()
df_result["id"] = df_issues_test["id"]
df_result[ISSUES_TARGET] = y_pred
#df_result.to_csv('solution_mljar.csv', index=False)
df_result
