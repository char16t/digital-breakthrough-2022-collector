# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
|              | [1_Baseline](1_Baseline/README.md)                           | Baseline       | r2            |    -0.00339604 |         1.51 |
|              | [2_DecisionTree](2_DecisionTree/README.md)                   | Decision Tree  | r2            |    -0.0687663  |        14.48 |
|              | [3_Linear](3_Linear/README.md)                               | Linear         | r2            |    -0.0345693  |         6.66 |
|              | [4_Default_Xgboost](4_Default_Xgboost/README.md)             | Xgboost        | r2            |    -0.0158932  |         7.96 |
|              | [5_Default_NeuralNetwork](5_Default_NeuralNetwork/README.md) | Neural Network | r2            |    -0.0272082  |         2.07 |
|              | [6_Default_RandomForest](6_Default_RandomForest/README.md)   | Random Forest  | r2            |    -0.024995   |         3.83 |
| **the best** | [Ensemble](Ensemble/README.md)                               | Ensemble       | r2            |     0.0133906  |         0.55 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

