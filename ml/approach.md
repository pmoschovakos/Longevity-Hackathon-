<<<<<<< HEAD
# ML Approach

## 1. Problem Formulation
We frame the task as a patient-level risk stratification problem.

Input: labs, demographics, comorbidities, derived liver scores.
Output: probability of MASH/CKM high-risk status.

## 2. Baseline
Clinical rule-based scores:
- FIB-4
- APRI
- AST/ALT ratio

## 3. Supervised Model
Primary model:
- XGBoost classifier

Why:
- strong for tabular clinical data
- handles nonlinear interactions
- works well with missing/noisy features
- compatible with SHAP explanations

## 4. Unsupervised / Exploratory Model
Autoencoder or clustering to identify unusual patient profiles and hidden risk groups.

## 5. Validation
- train/test split
- AUROC
- precision
- recall
- F1
- confusion matrix
- calibration if time allows

## 6. Explainability
Use SHAP and feature importance to show why a patient was flagged.

## 7. Clinical Integration
The model does not diagnose.
It flags patients for review, further testing, or specialist referral.
=======
# Machine Learning Methodology: Clinical Triage for MASH-CKM

## 1. Architectural Objective
This project implements an end-to-end predictive machine learning pipeline designed to distinguish MASH-CKM from other liver conditions using clinical markers sourced from the MIMIC III database. The architecture prioritizes data privacy, strict validation boundaries, and clinical explainability.

## 2. Data Privacy & Local Augmentation (The Security Split)
To strictly adhere to clinical data privacy constraints while overcoming sample size limitations, we implemented a secure, localized synthetic data generation strategy.
* **The Test Vault:** Before any augmentation occurred, the dataset underwent a strict 80/20 `GroupShuffleSplit` (grouped by `subject_id`). This locked a pure, unadulterated human testing vault away from the training pipeline, guaranteeing zero data leakage.
* **Local Inference:** Synthetic patient generation and unstructured NLP extraction were executed locally utilizing a Qwen2.5 LLM engine. By running this entirely on local hardware, we guaranteed that zero sensitive patient data was ever transmitted to external APIs.

#### Disclamer: this version runs on apple silicon chips.

## 3. Preprocessing & Feature Engineering
* **Missing Data:** Clinical labs routinely contain missing values. We utilized Multivariate Imputation by Chained Equations (MICE) via `IterativeImputer` to robustly estimate missing continuous variables.
* **Deterministic Engineering:** Complex biological proxies (such as the FIB-4 score, APRI score, and AST/ALT ratios) were engineered deterministically using native Pandas vectorization. This entirely mitigates the risk of "LLM math hallucinations" during the feature extraction phase.

## 4. Modeling Strategy (XGBoost)
The core predictive engine is an optimized binary `XGBClassifier`.
* **Imbalance Handling:** The model dynamically calculates and applies `scale_pos_weight` to counteract class imbalances between MASH-CKM and alternative liver diseases.
* **Validation:** Training utilized Stratified K-Fold cross-validation to ensure consistent class distributions across folds.
* **Threshold Optimization:** Rather than relying on a static 0.5 decision boundary, the pipeline dynamically calculates the optimal probability threshold by maximizing the Macro F1-Score on the validation distribution.

## 5. Clinical Explainability (SHAP)
A "black box" model is unacceptable in the clinical world. We integrated TreeExplainer SHAP (SHapley Additive exPlanations) directly into the native C++ Booster backend to provide:
* **Global Explainability:** Highlighting the systemic impact of features like FIB-4 and Platelets across the entire patient cohort.
* **Local Explainability:** Generating patient-specific waterfall plots to visually explain the exact clinical drivers behind every individual algorithmic diagnosis.
>>>>>>> 1155f08 (build(architecture): establish production directory structure and ML methodology)
