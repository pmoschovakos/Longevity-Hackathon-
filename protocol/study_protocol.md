# Study Protocol: Retrospective Triage Modeling for MASH-CKM

## 1. Background and Rationale
Metabolic dysfunction-associated steatohepatitis (MASH) combined with cardiovascular-kidney-metabolic (CKM) syndrome presents a severe, compounding clinical risk. Early identification in critical care settings is frequently missed due to the noise of acute admission data. This study aims to validate a machine learning triage pipeline capable of passively identifying high-risk MASH-CKM patients using standard, non-invasive admission labs.

## 2. Study Objectives
* **Primary Endpoint:** To develop a predictive binary classifier capable of distinguishing MASH-CKM from Alcoholic Liver Disease and other hepatic conditions with a Macro F1-Score > 0.80.
* **Secondary Endpoint:** To successfully automate the extraction of structured biomarker data (AST, ALT, Platelets, etc.) from unstructured clinical narrative notes using a localized LLM (Qwen2.5), completely bypassing the need for manual chart review.

## 3. Study Population & Design
* **Design:** Retrospective cohort study and synthetic augmentation pipeline.
* **Data Source:** MIMIC III (Medical Information Mart for Intensive Care) database.
* **Inclusion Criteria:** Adult patients (Age ≥ 18) admitted to critical care with a flagged hepatic or metabolic primary/secondary ICD-9 diagnostic code.
* **Exclusion Criteria:** Patients missing >25% of the designated baseline biomarker panel, rendering imputation statistically unreliable.

## 4. Methodology & Privacy Controls
To satisfy HIPAA and institutional data privacy constraints, no patient data was transmitted to external APIs.
1. **The Human Vault:** 20% of the viable cohort was strictly isolated using a `GroupShuffleSplit` prior to any data manipulation to serve as the ground-truth validation set.
2. **Local Synthetic Augmentation:** The training cohort was augmented using a locally hosted Apple Silicon LLM to balance class distributions without compromising patient data security. 
3. **Inference:** The final diagnostic threshold was dynamically optimized to prioritize sensitivity (recall) for the MASH-CKM minority class, ensuring critical cases are aggressively flagged for physician review.