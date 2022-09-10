# Summary of 105_RandomForest_Stacked

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 0.8
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

33.1 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13307.6         |
| MSE      |     5.03945e+09 |
| RMSE     | 70989.1         |
| R2       |    -0.0147941   |
| MAPE     |     1.58657     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
