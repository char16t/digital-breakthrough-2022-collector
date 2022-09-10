# Summary of 52_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Regressor (Extra Trees)
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 1.0
- **min_samples_split**: 40
- **max_depth**: 7
- **eval_metric_name**: r2
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

9.9 seconds

### Metric details:
| Metric   |          Score |
|:---------|---------------:|
| MAE      | 13320.8        |
| MSE      |     5.0429e+09 |
| RMSE     | 71013.4        |
| R2       |    -0.0154887  |
| MAPE     |     1.58422    |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
