# Summary of 40_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 1.0
- **min_samples_split**: 40
- **max_depth**: 6
- **eval_metric_name**: r2
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

9.7 seconds

### Metric details:
| Metric   |          Score |
|:---------|---------------:|
| MAE      | 13316.1        |
| MSE      |     5.0418e+09 |
| RMSE     | 71005.6        |
| R2       |    -0.0152682  |
| MAPE     |     1.58482    |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
