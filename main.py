#!/usr/bin/env python3

import numpy as np
import pandas as pd

df_issues_train = pd.read_csv("data/train_issues.csv")
df_comment_train = pd.read_csv("data/train_comments.csv")
df_emp = pd.read_csv("data/employees.csv")
df_issues_test = pd.read_csv("data/test_issues.csv")
df_comment_test = pd.read_csv("data/test_comments.csv")

merged = pd.merge(df_issues_train, df_emp.add_prefix('assignee_'), left_on="assignee_id", right_on="assignee_id", how='inner')
merged = pd.merge(merged, df_emp.add_prefix('creator_'), left_on="creator_id", right_on="creator_id", how='inner')
merged.to_csv('target/merged.csv', index=False)

df_result = pd.DataFrame()
df_result["id"] = df_issues_test["id"]
df_result["overall_worklogs"] = 0
df_result.to_csv('target/solution.csv', index=False)
