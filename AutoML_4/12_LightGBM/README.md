# Summary of 12_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: regression
- **num_leaves**: 15
- **learning_rate**: 0.1
- **feature_fraction**: 0.8
- **bagging_fraction**: 0.5
- **min_data_in_leaf**: 5
- **metric**: custom
- **custom_eval_metric_name**: r2
- **explain_level**: 2

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
r2

## Training time

12.3 seconds

### Metric details:
| Metric   |           Score |
|:---------|----------------:|
| MAE      | 13159.1         |
| MSE      |     5.01781e+09 |
| RMSE     | 70836.5         |
| R2       |    -0.0104369   |
| MAPE     |     1.51406     |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)
### Dependence (Fold 2)
![SHAP Dependence from Fold 2](learner_fold_1_shap_dependence.png)
### Dependence (Fold 3)
![SHAP Dependence from Fold 3](learner_fold_2_shap_dependence.png)
### Dependence (Fold 4)
![SHAP Dependence from Fold 4](learner_fold_3_shap_dependence.png)
### Dependence (Fold 5)
![SHAP Dependence from Fold 5](learner_fold_4_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions (Fold 1)
![SHAP worst decisions from fold 1](learner_fold_0_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 2)
![SHAP worst decisions from fold 2](learner_fold_1_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 3)
![SHAP worst decisions from fold 3](learner_fold_2_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 4)
![SHAP worst decisions from fold 4](learner_fold_3_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold 5)
![SHAP worst decisions from fold 5](learner_fold_4_shap_worst_decisions.png)
### Top-10 Best decisions (Fold 1)
![SHAP best decisions from fold 1](learner_fold_0_shap_best_decisions.png)
### Top-10 Best decisions (Fold 2)
![SHAP best decisions from fold 2](learner_fold_1_shap_best_decisions.png)
### Top-10 Best decisions (Fold 3)
![SHAP best decisions from fold 3](learner_fold_2_shap_best_decisions.png)
### Top-10 Best decisions (Fold 4)
![SHAP best decisions from fold 4](learner_fold_3_shap_best_decisions.png)
### Top-10 Best decisions (Fold 5)
![SHAP best decisions from fold 5](learner_fold_4_shap_best_decisions.png)

[<< Go back](../README.md)
