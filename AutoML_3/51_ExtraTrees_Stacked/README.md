# Summary of 51_ExtraTrees_Stacked

[<< Go back](../README.md)


## Extra Trees Regressor (Extra Trees)
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 0.7
- **min_samples_split**: 30
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

34.8 seconds

### Metric details:
| Metric   |          Score |
|:---------|---------------:|
| MAE      | 13297.4        |
| MSE      |     5.0373e+09 |
| RMSE     | 70973.9        |
| R2       |    -0.0143614  |
| MAPE     |     1.5817     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
