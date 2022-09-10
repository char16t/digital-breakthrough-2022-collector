# Summary of 81_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 0.8
- **min_samples_split**: 50
- **max_depth**: 3
- **eval_metric_name**: r2
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **k_folds**: 10

## Optimized metric
r2

## Training time

19.6 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13311.2         |
| MSE      |     5.04204e+09 |
| RMSE     | 71007.3         |
| R2       |    -0.0153153   |
| MAPE     |     1.58267     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
