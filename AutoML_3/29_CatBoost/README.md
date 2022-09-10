# Summary of 29_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.05
- **depth**: 8
- **rsm**: 0.8
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

8.4 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13307.6         |
| MSE      |     5.04473e+09 |
| RMSE     | 71026.3         |
| R2       |    -0.0158576   |
| MAPE     |     1.58088     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
