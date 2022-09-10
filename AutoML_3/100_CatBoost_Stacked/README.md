# Summary of 100_CatBoost_Stacked

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
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

33.0 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13312           |
| MSE      |     5.04314e+09 |
| RMSE     | 71015.1         |
| R2       |    -0.0155372   |
| MAPE     |     1.64809     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
