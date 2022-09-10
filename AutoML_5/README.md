# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
|              | [1_Baseline](1_Baseline/README.md)                           | Baseline       | r2            |    -0.00339604 |         1.61 |
|              | [2_DecisionTree](2_DecisionTree/README.md)                   | Decision Tree  | r2            |    -0.0216861  |        13.37 |
|              | [3_Linear](3_Linear/README.md)                               | Linear         | r2            |    -0.0347007  |         7.55 |
|              | [4_Default_Xgboost](4_Default_Xgboost/README.md)             | Xgboost        | r2            |    -0.0174178  |         7.17 |
|              | [5_Default_NeuralNetwork](5_Default_NeuralNetwork/README.md) | Neural Network | r2            |    -0.0246056  |         2.04 |
|              | [6_Default_RandomForest](6_Default_RandomForest/README.md)   | Random Forest  | r2            |    -0.02493    |         3.77 |
| **the best** | [Ensemble](Ensemble/README.md)                               | Ensemble       | r2            |     0.0242705  |         0.54 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)
