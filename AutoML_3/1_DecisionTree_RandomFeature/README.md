# Summary of 1_DecisionTree_RandomFeature

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: mse
- **max_depth**: 3
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

52.1 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 16481.7         |
| MSE      |     4.95865e+09 |
| RMSE     | 70417.6         |
| R2       |     0.0014771   |
| MAPE     |     4.12974     |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
