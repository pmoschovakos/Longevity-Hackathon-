import pandas as pd

print("--- 1. Loading Datasets ---")
# Load your original MIMIC III data
try:
    df_real = pd.read_csv("main.csv")
    print(f"Loaded {len(df_real)} real patients.")
except FileNotFoundError:
    print("❌ Error: Could not find 'main.csv'. Make sure it is in the same folder.")
    exit()

# Load the synthetic data you saved from the Jupyter Notebook
try:
    df_synthetic = pd.read_csv("synthetic_patients_qwen.csv")
    print(f"Loaded {len(df_synthetic)} synthetic patients.")
except FileNotFoundError:
    print("❌ Error: Could not find 'synthetic_patients_qwen.csv'. Did you run the save cell in your notebook?")
    exit()

print("\n--- 2. Formatting Synthetic IDs & Missing Columns ---")
# Generate fake IDs so the columns align, but tag them so they are obviously synthetic
df_synthetic['subject_id'] = ["SYN_SUB_" + str(i) for i in range(len(df_synthetic))]
df_synthetic['hadm_id'] = ["SYN_HADM_" + str(i) for i in range(len(df_synthetic))]

# If there are any other text columns in the real data (like short_title or long_title) 
# that Qwen didn't generate, we fill them with a placeholder to keep the tables mathematically aligned.
for col in df_real.columns:
    if col not in df_synthetic.columns:
        df_synthetic[col] = "SYNTHETIC_GENERATED"

# Force the synthetic dataset to have the exact same column order as the real dataset
df_synthetic = df_synthetic[df_real.columns]

print("\n--- 3. Merging the Datasets ---")
# Stack them vertically
df_merged = pd.concat([df_real, df_synthetic], ignore_index=True)

print("\n--- 4. Saving to Disk ---")
output_filename = "main_augmented_full.csv"
df_merged.to_csv(output_filename, index=False)

print(f"✅ Success! Saved massive merged dataset to: {output_filename}")
print(f"Total records in new file: {len(df_merged)}")