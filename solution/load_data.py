import pandas as pd
from sklearn.model_selection import train_test_split

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
