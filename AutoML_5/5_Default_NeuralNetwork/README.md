# Summary of 5_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True

## Optimized metric
r2

## Training time

1.2 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 11575.4         |
| MSE      |     1.76853e+09 |
| RMSE     | 42053.9         |
| R2       |    -0.0246056   |
| MAPE     |     1.8497      |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
