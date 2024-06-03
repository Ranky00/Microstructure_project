####Extracted FDR_P-value
import pandas as pd
data1=pd.read_csv('/Users/demoranky/documents/water_LBP/combined_LBP_results_PCA__with_ratio_LM.csv')
p_value_rows = data1[data1['Statistic'].str.contains('P-value', case=False, na=False)]
#p_value_rows.to_csv('/Users/demoranky/documents/water_LBP/combined_LBP_results_PCA__with_ratio_LM_P-values.csv', index=False, float_format='%g')




import pandas as pd
from statsmodels.stats.multitest import fdrcorrection


# Read data from CSV file
data =  p_value_rows

# Select columns containing p-values (replace with actual column names)
p_value_cols = ['PC1_WM', 'PC1_GM', 'PC2_WM', 'PC2_GM']
p_values = data[p_value_cols]

# Initialize a DataFrame to store adjusted p-values
adjusted_data = pd.DataFrame(index=data.index)

# Perform FDR correction (Benjamini-Hochberg method) for each column separately
for col in p_value_cols:
    pvals = data[col].values
    _, fdr_adjusted_pvalues = fdrcorrection(pvals)
    adjusted_data[f"{col}_adjusted_pvalue"] = fdr_adjusted_pvalues

# Optional: Include original p-values if needed
for col in p_value_cols:
    adjusted_data[f"{col}_original_pvalue"] = data[col]

# Print the adjusted data
print(adjusted_data)

# Optional: Save the adjusted data to a new CSV file
adjusted_data.to_csv("/Users/demoranky/documents/combined_LBP_PCA_results_with_ratio_adjusted_pvalues.csv", index=True)
