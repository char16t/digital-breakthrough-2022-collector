import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML

from solution.load_data import \
    df_issues_train, \
    df_comment_train, \
    df_emp, \
    df_issues_test, \
    df_comment_test, \
    merged

X_train, X_test, y_train, y_test = train_test_split(
    merged[['project_id']],
    merged[['overall_worklogs']],
    test_size=0.33, 
    random_state=42,
)

automl = AutoML()
automl.fit(X_train, y_train)

predictions = automl.predict(X_test)
