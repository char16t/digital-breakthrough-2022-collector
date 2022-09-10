# Summary of 86_ExtraTrees_Stacked

[<< Go back](../README.md)


## Extra Trees Regressor (Extra Trees)
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 0.9
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

39.4 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13305.2         |
| MSE      |     5.04086e+09 |
| RMSE     | 70999           |
| R2       |    -0.0150786   |
| MAPE     |     1.5736      |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
