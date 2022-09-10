# Summary of 40_RandomForest_Stacked

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

37.1 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13308           |
| MSE      |     5.04112e+09 |
| RMSE     | 71000.9         |
| R2       |    -0.0151314   |
| MAPE     |     1.57602     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
