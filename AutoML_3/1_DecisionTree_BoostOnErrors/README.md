# Summary of 1_DecisionTree_BoostOnErrors

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: mse
- **max_depth**: 3
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

16.7 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 16664.9         |
| MSE      |     4.93239e+09 |
| RMSE     | 70231           |
| R2       |     0.00676332  |
| MAPE     |     4.32052     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
