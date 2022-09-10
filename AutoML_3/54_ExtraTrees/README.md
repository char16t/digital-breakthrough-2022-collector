# Summary of 54_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Regressor (Extra Trees)
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 0.6
- **min_samples_split**: 20
- **max_depth**: 4
- **eval_metric_name**: r2
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

12.3 seconds

### Metric details:
| Metric   |          Score |
|:---------|---------------:|
| MAE      | 13315.5        |
| MSE      |     5.0433e+09 |
| RMSE     | 71016.2        |
| R2       |    -0.0155698  |
| MAPE     |     1.58264    |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
