# Summary of 45_RandomForest

[<< Go back](../README.md)


## Random Forest
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

15.9 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13316.8         |
| MSE      |     5.04252e+09 |
| RMSE     | 71010.7         |
| R2       |    -0.0154135   |
| MAPE     |     1.58639     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
