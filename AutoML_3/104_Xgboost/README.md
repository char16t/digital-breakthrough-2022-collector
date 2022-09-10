# Summary of 104_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: reg:squarederror
- **eta**: 0.1
- **max_depth**: 7
- **min_child_weight**: 50
- **subsample**: 0.6
- **colsample_bytree**: 0.6
- **eval_metric**: r2
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

37.4 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13310.7         |
| MSE      |     5.04092e+09 |
| RMSE     | 70999.4         |
| R2       |    -0.0150904   |
| MAPE     |     1.60956     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
