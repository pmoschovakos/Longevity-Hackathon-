# Slide Deck Outline: Clinical Triage for MASH-CKM

## Slide 1: Title & Vision
* **Title:** AI-Driven Clinical Triage for MASH-CKM
* **Subtitle:** Privacy-First Predictive Modeling using MIMIC III
* **The Hook:** Metabolic dysfunction-associated steatohepatitis (MASH) is a silent compounding risk in critical care. We built a pipeline to flag it automatically, securely, and transparently.

## Slide 2: The Clinical Problem
* **The Noise:** Intensive care data is overwhelming; secondary metabolic conditions are frequently missed.
* **The Challenge:** How do we predict MASH-CKM risk using only standard admission labs (AST, ALT, Platelets) without violating patient data privacy?
* **The Goal:** A passive triage system that alerts physicians to high-risk patients without requiring manual chart reviews.

## Slide 3: The Architecture & Privacy Shield
* **The "Security Split":** Before any modeling occurred, 20% of the cohort was locked in a secure validation vault to guarantee zero data leakage.
* **Local LLM Augmentation:** Overcame class imbalance and data scarcity by generating synthetic medical records using **Qwen2.5 (7b)** running entirely locally on Apple Silicon. 
* **Zero External APIs:** No sensitive patient data ever left the local machine, strictly adhering to HIPAA/GDPR constraints.

## Slide 4: Feature Engineering & Extraction
* **Physician-Guided:** Features were not selected at random; a dedicated medical team flagged critical biomarkers (Hepatic, Coagulation, Metabolic).
* **Deterministic Math:** Complex clinical proxies like the FIB-4 and APRI scores were calculated natively in Python to prevent LLM math hallucinations.
* **Unstructured NLP:** Demonstrated the ability to parse raw, unstructured clinical narrative notes into structured JSON using local LLM inference.

## Slide 5: The Predictive Engine (XGBoost)
* **The Model:** Optimized XGBoost Classifier handling extreme class imbalances.
* **Dynamic Thresholding:** Rather than a static 0.5 decision boundary, the pipeline dynamically calculates the optimal threshold to maximize the Macro F1-Score, prioritizing the capture of critical MASH-CKM cases.

## Slide 6: Breaking the Black Box (Explainability)
* **Why it matters:** Physicians do not trust black boxes.
* **Global SHAP:** Demonstrating how systemic factors (like high FIB-4 and low Platelets) drive the model's logic across the entire population.
* **Local SHAP (Waterfall Plots):** Generating a personalized clinical breakdown for *every single patient*, showing the exact biological drivers behind their specific risk score.

## Slide 7: Live Inference Demo & Future Impact
* **The Demo:** (Run Cell 11 in the Jupyter Notebook to show the end-to-end automated triage report).
* **Impact:** A scalable, privacy-safe, and explainable AI tool ready for deployment in real-world critical care networks.