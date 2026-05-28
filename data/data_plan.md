# Clinical Data Plan: MIMIC III & Feature Engineering

## 1. Data Provenance
All raw clinical data utilized in this pipeline was sourced from the **MIMIC III (Medical Information Mart for Intensive Care)** database. This provides a robust, real-world foundation of de-identified critical care health data for predictive modeling.

## 2. Physician-Guided Feature Selection
To ensure clinical relevance and physiological accuracy, all baseline features were strictly curated and flagged by a collaborative team of physicians prior to modeling. The selected biomarker panel includes:
* **Hepatic Markers:** AST, ALT, Total Bilirubin, Albumin
* **Coagulation & Hematology:** Platelets, INR
* **Metabolic & Renal:** Glucose, Creatinine
* **Demographics:** Age, Gender

## 3. Data Scrubbing & Imputation
Clinical real-world data is inherently noisy.
* **Scrubbing:** Bracketed values and text-based lab artifacts were programmatically stripped and safely coerced into continuous numeric types.
* **Missingness:** Patients missing >25% of the targeted biomarker panel were dropped to preserve cohort integrity. 
* **Imputation:** For patients with acceptable missingness, we deployed **MICE (Multivariate Imputation by Chained Equations)** via Scikit-Learn's `IterativeImputer` to predict missing lab values based on the covariance of the entire clinical panel.

## 4. Complex Feature Engineering
Rather than relying on raw labs alone, we deterministically engineered established clinical scoring systems natively in Pandas:
* **FIB-4 Score:** `(Age * AST) / (Platelets * sqrt(ALT))` - A standard non-invasive proxy for liver fibrosis.
* **APRI Score:** `(AST / 40.0) / Platelets * 100` - AST to Platelet Ratio Index.
* **AST/ALT Ratio:** Identifies potential alcoholic etiology vs. non-alcoholic steatohepatitis.
* **Metabolic Risk & Severity Proxies:** Binary flags generated for senior age thresholds, thrombocytopenia presence, and glucose-driven metabolic risk.