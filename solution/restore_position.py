import math
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import simple_preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from sklearn.linear_model import LogisticRegression
import nltk
nltk.download('punkt')

df_issues_train = pd.read_csv("/content/drive/MyDrive/champ/collector/train_issues.csv")
df_comment_train = pd.read_csv("/content/drive/MyDrive/champ/collector/train_comments.csv")
df_emp = pd.read_csv("/content/drive/MyDrive/champ/collector/employees.csv")
df_issues_test = pd.read_csv("/content/drive/MyDrive/champ/collector/test_issues.csv")
df_comment_test = pd.read_csv("/content/drive/MyDrive/champ/collector/test_comments.csv")

merged = pd.merge(df_issues_train, df_emp.add_prefix('assignee_'), left_on="assignee_id", right_on="assignee_id", how='inner')
merged = pd.merge(merged, df_emp.add_prefix('creator_'), left_on="creator_id", right_on="creator_id", how='inner')
#merged.to_csv("merged.csv", index=False)

def tag_docs(docs, col):
    tagged = docs.apply(lambda r: TaggedDocument(words=simple_preprocess(r[col]), tags=[r['assignee_position']]), axis=1)
    return tagged

def train_doc2vec_model(tagged_docs, window, size):
    sents = tagged_docs.values
    doc2vec_model = Doc2Vec(sents, size=size, window=window, iter=20, dm=1)
    return doc2vec_model

def vec_for_learning(doc2vec_model, tagged_docs):
    sents = tagged_docs.values
    targets, regressors = zip(*[(doc.tags[0], doc2vec_model.infer_vector(doc.words, steps=20)) for doc in sents])
    return targets, regressors

merged_f = merged[merged['assignee_position'].notnull()]

X = merged_f['summary']
y = merged_f['assignee_position']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
vectorizer = TfidfVectorizer(stop_words='english')
X_train_dtm = vectorizer.fit_transform(X_train)
X_test_dtm = vectorizer.transform(X_test)

clf_lr = LogisticRegression()
clf_lr.fit(X_train_dtm, y_train)
y_pred = clf_lr.predict(X_test_dtm)

from sklearn.metrics import accuracy_score
print("accuracy_score =", accuracy_score(y_test, y_pred))

df1 = merged[merged['assignee_position'].isnull()]
y_pred = clf_lr.predict(vectorizer.transform(df1['summary']))
df1['assignee_position'] = y_pred
df1[['assignee_id', 'assignee_position']].head(3)

idx = df1.groupby('assignee_id')['assignee_position'].agg(size= len, set= lambda x: list(x)).reset_index()

def get_positions_by_assignee_id(assignee_id):
  found = idx[idx['assignee_id'] == assignee_id]['set'].to_numpy()
  if found.size == 0:
    return []
  else:
    return found[0]

def get_position_by_assignee_id(assignee_id):
  arr = get_positions_by_assignee_id(assignee_id)
  u, indices = np.unique(arr, return_inverse=True)
  return u[np.argmax(np.bincount(indices))]

# creator id
merged_f = merged[merged['creator_position'].notnull()]

X = merged_f['summary']
y = merged_f['creator_position']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
vectorizer = TfidfVectorizer(stop_words='english')
X_train_dtm = vectorizer.fit_transform(X_train)
X_test_dtm = vectorizer.transform(X_test)

clf_lr2 = LogisticRegression()
clf_lr2.fit(X_train_dtm, y_train)
y_pred = clf_lr2.predict(X_test_dtm)

df2 = merged[merged['creator_position'].isnull()]
y_pred2 = clf_lr2.predict(vectorizer.transform(df2['summary']))
df2['creator_position'] = y_pred2

idx2 = df2.groupby('creator_id')['creator_position'].agg(size= len, set= lambda x: list(x)).reset_index()

def get_positions_by_creator_id(creator_id):
  found = idx2[idx2['creator_id'] == creator_id]['set'].to_numpy()
  if found.size == 0:
    return []
  else:
    return found[0]

def get_position_by_creator_id(creator_id):
  arr = get_positions_by_creator_id(creator_id)
  u, indices = np.unique(arr, return_inverse=True)
  return u[np.argmax(np.bincount(indices))]

def get_position(user_id):
  assignee_positions = get_positions_by_assignee_id(user_id)
  creator_positions = get_positions_by_creator_id(user_id)
  positions = np.concatenate((assignee_positions, creator_positions))
  u, indices = np.unique(positions, return_inverse=True)
  return u[np.argmax(np.bincount(indices))]

# merged['assignee_position'].fillna(merged['assignee_id'].map(lambda x: get_position(x)))
# merged['creator_position'].fillna(merged['creator_id'].map(lambda x: get_position(x)))

merged['assignee_position'] = merged.apply(lambda row: get_position(row['assignee_id']) if pd.isnull(row['assignee_position']) else row['assignee_position'], axis=1)
merged['creator_position'] = merged.apply(lambda row: get_position(row['creator_id']) if pd.isnull(row['creator_position']) else row['creator_position'], axis=1)


#df2[['creator_id', 'creator_position']].head(3)
#merged.apply(lambda row: get_position(row["assignee_id"]) if row["assignee_id"].isnull() else row["assignee_position"], axis=1)
#merged

