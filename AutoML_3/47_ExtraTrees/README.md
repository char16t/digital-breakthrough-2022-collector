# Summary of 47_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Regressor (Extra Trees)
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 0.5
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

7.7 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13318.4         |
| MSE      |     5.04325e+09 |
| RMSE     | 71015.9         |
| R2       |    -0.0155604   |
| MAPE     |     1.58403     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
