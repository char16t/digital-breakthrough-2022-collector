# Summary of 101_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
- **depth**: 6
- **rsm**: 1.0
- **loss_function**: MAE
- **eval_metric**: R2
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

29.8 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13310.7         |
| MSE      |     5.04047e+09 |
| RMSE     | 70996.3         |
| R2       |    -0.0150006   |
| MAPE     |     1.65295     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
