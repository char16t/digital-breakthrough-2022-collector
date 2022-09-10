# Summary of 106_ExtraTrees_Stacked

[<< Go back](../README.md)


## Extra Trees Regressor (Extra Trees)
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 0.7
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

35.2 seconds

### Metric details:
| Metric   |        Score |
|:---------|-------------:|
| MAE      | 13301        |
| MSE      |     5.04e+09 |
| RMSE     | 70992.9      |
| R2       |    -0.014905 |
| MAPE     |     1.56314  |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
