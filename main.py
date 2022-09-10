#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

from solution.logging import rootLogger
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


dd = merged.groupby(['project_id'])['overall_worklogs'].agg('median').reset_index()
def getMedian(pid): 
    return dd[dd['project_id'] == pid]['overall_worklogs'].iloc[0].astype(np.int64)

y_pred = X_test[['id', 'project_id']].apply(lambda row: getMedian(row['project_id']), axis=1)
rootLogger.warning("R2 metric: " + str(r2_score(y_test, y_pred)))

df_result = pd.DataFrame()
df_result["id"] = df_issues_test["id"]
df_result["overall_worklogs"] = df_issues_test.apply(lambda row: getMedian(row['project_id']), axis=1)
df_result.to_csv('target/solution.csv', index=False)
