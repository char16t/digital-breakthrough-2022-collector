#!/usr/bin/env python3

from distutils.debug import DEBUG
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import logging

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler("{0}/{1}.log".format('target', 'solution'))
fileHandler.setFormatter(logFormatter)
fileHandler.setLevel(logging.NOTSET)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
consoleHandler.setLevel(logging.NOTSET)
rootLogger.addHandler(consoleHandler)


df_issues_train = pd.read_csv("data/train_issues.csv")
df_comment_train = pd.read_csv("data/train_comments.csv")
df_emp = pd.read_csv("data/employees.csv")
df_issues_test = pd.read_csv("data/test_issues.csv")
df_comment_test = pd.read_csv("data/test_comments.csv")

merged = pd.merge(df_issues_train, df_emp.add_prefix('assignee_'), left_on="assignee_id", right_on="assignee_id", how='inner')
merged = pd.merge(merged, df_emp.add_prefix('creator_'), left_on="creator_id", right_on="creator_id", how='inner')
merged.to_csv('target/merged.csv', index=False)

X_train, X_test, y_train, y_test = train_test_split(
    merged.drop('overall_worklogs', axis=1),
    merged[['overall_worklogs']],
    test_size=0.33, 
    random_state=42,
)

dd = merged.groupby(['project_id'])['overall_worklogs'].agg('median').reset_index()
def getMedian(pid): 
    return dd[dd['project_id'] == pid]['overall_worklogs'].iloc[0].astype(np.int64)

y_pred = X_test[['id', 'project_id']].apply(lambda row: getMedian(row['project_id']), axis=1)
rootLogger.warn("R2 metric: " + str(r2_score(y_test, y_pred)))

df_result = pd.DataFrame()
df_result["id"] = df_issues_test["id"]
df_result["overall_worklogs"] = df_issues_test.apply(lambda row: getMedian(row['project_id']), axis=1)
df_result.to_csv('target/solution.csv', index=False)
