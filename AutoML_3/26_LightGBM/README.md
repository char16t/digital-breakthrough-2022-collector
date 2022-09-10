# Summary of 26_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: regression
- **num_leaves**: 63
- **learning_rate**: 0.05
- **feature_fraction**: 0.9
- **bagging_fraction**: 0.8
- **min_data_in_leaf**: 30
- **metric**: custom
- **custom_eval_metric_name**: r2
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

16.1 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13309           |
| MSE      |     5.04572e+09 |
| RMSE     | 71033.2         |
| R2       |    -0.0160574   |
| MAPE     |     1.57978     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
