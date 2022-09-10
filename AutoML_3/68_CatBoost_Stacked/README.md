# Summary of 68_CatBoost_Stacked

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 5
- **rsm**: 0.7
- **loss_function**: MAPE
- **eval_metric**: R2
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

29.2 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13311.8         |
| MSE      |     5.03944e+09 |
| RMSE     | 70989           |
| R2       |    -0.0147933   |
| MAPE     |     1.68398     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
