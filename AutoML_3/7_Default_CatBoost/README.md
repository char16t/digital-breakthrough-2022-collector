# Summary of 7_Default_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
- **rsm**: 1
- **loss_function**: RMSE
- **eval_metric**: R2
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

5.9 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13308.6         |
| MSE      |     5.04497e+09 |
| RMSE     | 71028           |
| R2       |    -0.0159062   |
| MAPE     |     1.5805      |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
