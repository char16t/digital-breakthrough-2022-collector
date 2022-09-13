#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk

from solution.logging import rootLogger
from solution.train_doc2vec_summary import build_d2v_summary_model 
from solution.load_data import \
    df_issues_train, \
    df_comment_train, \
    df_emp, \
    df_issues_test, \
    df_comment_test, \
    merged, \
    X_train, \
    X_test, \
    y_train, \
    y_test


build_d2v_summary_model()
build_d2v_comments_model()

model= Doc2Vec.load("target/summary.d2v.model")

def cast_vector(row):
    r = np.array(list(map(lambda x: x.astype('double'), row)))
    return r
    
def to_vec(text):
  test_data = word_tokenize(text.lower())
  return cast_vector(model.infer_vector(test_data))

vectors = []
for s in merged["summary"]:
  vectors.append(to_vec(s))
vecs = pd.DataFrame(vectors)
#vecs.head()
merged["summary_vectorized"] = vectors

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=100, random_state=42) 
kmeans.fit(vecs)

res = pd.DataFrame()
res["kmean"] = kmeans.labels_
res['kmean'].value_counts()
merged["summary_cluster"] = res["kmean"]


X_train, X_test, y_train, y_test = train_test_split(
    merged[['project_id', 'summary_cluster']],
    merged[['overall_worklogs']],
    test_size=0.33, 
    random_state=42,
)


from sklearn.dummy import DummyRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from xgboost import XGBRegressor

for strategy in ["mean", "median"]:
  dummy = DummyRegressor(strategy=strategy)
  dummy.fit(X_train, y_train)
  y_pred = dummy.predict(X_test)
  print("DummyRegressor [strategy=" + strategy + "], R2: " + str(r2_score(y_test, y_pred)))

regressor = DecisionTreeRegressor(random_state=42)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("DecisionTreeRegressor, R2: " + str(r2_score(y_test, y_pred)))

reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print("LinearRegression, R2: " + str(r2_score(y_test, y_pred)))

bst = XGBRegressor()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print("XGBRegressor, R2: " + str(r2_score(y_test, y_pred)))

reg = RandomForestRegressor()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print("RandomForestRegressor, R2: " + str(r2_score(y_test, y_pred)))




dd = merged.groupby(['project_id'])['overall_worklogs'].agg('median').reset_index()
def getMedian(pid): 
    return dd[dd['project_id'] == pid]['overall_worklogs'].iloc[0].astype(np.int64)

y_pred = X_test[['id', 'project_id']].apply(lambda row: getMedian(row['project_id']), axis=1)
rootLogger.warning("My median R2 metric: " + str(r2_score(y_test, y_pred)))

df_result = pd.DataFrame()
df_result["id"] = df_issues_test["id"]
df_result["overall_worklogs"] = df_issues_test.apply(lambda row: getMedian(row['project_id']), axis=1)
df_result.to_csv('target/solution.csv', index=False)
