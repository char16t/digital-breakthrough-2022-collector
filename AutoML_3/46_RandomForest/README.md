# Summary of 46_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 0.5
- **min_samples_split**: 10
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

15.8 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13315.6         |
| MSE      |     5.04331e+09 |
| RMSE     | 71016.3         |
| R2       |    -0.0155719   |
| MAPE     |     1.58035     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
