# Summary of 79_RandomForest_Stacked

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: mse
- **max_features**: 0.9
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

38.8 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13307.4         |
| MSE      |     5.04021e+09 |
| RMSE     | 70994.5         |
| R2       |    -0.0149481   |
| MAPE     |     1.58309     |



## Learning curves
![Learning curves](learning_curves.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
