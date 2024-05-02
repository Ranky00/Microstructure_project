###SUVR for A+

import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols

# Define paths for data files (modify as needed)
data_path_abc = "/location_of_data_IDM_TE.csv"
data_path_suvr = "/Users/demoranky/documents/Data_for_suvr_ABC/ABC_composite_SUVR_ready1.csv"
output_path1 = "/Users/demoranky/documents/Data_for_suvr_ABC/207_suvr_A+_LM.csv"###location to save LM result
output_path10 = "/Users/demoranky/documents/Data_for_suvr_ABC/207_suvr_A+_data.csv"##Location to save combined result
output_path11 = "/Users/demoranky/documents/Data_for_suvr_ABC/207_suvr_data.csv"###location to save S

# Read data from CSV files
df_abc = pd.read_csv(data_path_abc)
df_suvr = pd.read_csv(data_path_suvr)

# Combine datasets (consider using inner/outer join if needed)
df_combined = pd.concat([df_abc, df_suvr], axis=1)

# Filter data based on Amyloid_consensus (optional)
df_filtered = df_combined.loc[df_combined["Amyloid_consensus"] != "Negative"]  # Alternative: df_combined[df_combined["Amyloid_consensus"] != "Negative"]

# Function for statistical analysis (consider generalizing for multiple features)
def perform_stats(df, feature_name):
  model = ols(f"{feature_name}_GM ~ compSUVR + AgeatTest", data=df).fit()
  p_values = model.pvalues[1:]  # Exclude intercept
  t_values = abs(model.tvalues[1:])  # Absolute values for t-statistics
  return pd.DataFrame({"P-value": p_values, "T-value": t_values})

# Analyze features (TotalEnergy, IDM) for GM and WM
stats_gm = perform_stats(df_filtered, "TotalEnergy")
stats_wm = perform_stats(df_filtered, "IDM")

# Combine and format results
results = pd.concat([stats_gm, stats_wm], axis=1).T
results.rename(columns={"TotalEnergy_GM": "Negative_Mean", "TotalEnergy_WM": "Positive_Mean",
                         "IDM_GM": "Negative_Mean.1", "IDM_WM": "Positive_Mean.1"}, inplace=True)
results.rename(index={0: "Negative_SD", 1: "Positive_SD"}, inplace=True)
display(results)
# Save statistical results (consider separating data and stats)
results.to_csv(output_path1, index=True, float_format='%g')

# Save combined data (optional)
df_combined.to_csv(output_path10, index=False, float_format='%g')

# Save filtered data (optional)
df_filtered.to_csv(output_path11, index=False, float_format='%g')
