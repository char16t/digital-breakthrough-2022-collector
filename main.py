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


dd = merged.groupby(['project_id'])['overall_worklogs'].agg('median').reset_index()
def getMedian(pid): 
    return dd[dd['project_id'] == pid]['overall_worklogs'].iloc[0].astype(np.int64)

y_pred = X_test[['id', 'project_id']].apply(lambda row: getMedian(row['project_id']), axis=1)
rootLogger.warning("R2 metric: " + str(r2_score(y_test, y_pred)))

df_result = pd.DataFrame()
df_result["id"] = df_issues_test["id"]
df_result["overall_worklogs"] = df_issues_test.apply(lambda row: getMedian(row['project_id']), axis=1)
df_result.to_csv('target/solution.csv', index=False)
