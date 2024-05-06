import os
import pandas as pd
from statsmodels.formula.api import ols

# Define data paths
data_path_suvr = "/Users/demoranky/documents/Data_for_suvr_ABC/ABC_composite_SUVR_ready1.csv"
base_path_abc = "/Users/demoranky/documents/ABC_new_extract/final_"  # Base path for GM/WM data
base_output_path = "/Users/demoranky/documents/ABC_SUVR_May2024/"

def process_data(x_value):
    """
    Processes data for a given x value, including reading data, performing analysis, and saving results.

    Args:
        x_value (int): The value of x to use for file path construction.
    """
    # Construct file paths based on x_value
    data_path_abc = base_path_abc + f"{x_value}_GM_WM_used.csv"
    output_path1 = base_output_path + f"{x_value}_suvr_A+_LM.csv"
    output_path11 = base_output_path + f"{x_value}_suvr_A+_data.csv"
    output_path10 = base_output_path + f"{x_value}_suvr_data.csv"

    # Read data from CSV files
    df_abc = pd.read_csv(data_path_abc)
    df_suvr = pd.read_csv(data_path_suvr)

    # Combine datasets
    df_combined = pd.concat([df_abc, df_suvr], axis=1)

    # Filter data based on Amyloid_s_th
    df_filtered = df_combined.loc[df_combined["Amyloid_s_th"] != "Negative"]

    # Function for statistical analysis
    model1a = ols('TotalEnergy_GM ~ compSUVR + AGE', data=df_filtered).fit() 
    model1b = ols('TotalEnergy_WM ~ compSUVR + AGE', data=df_filtered).fit()
    model2a = ols('IDM_GM ~ compSUVR + AGE', data=df_filtered).fit()
    model2b = ols('IDM_WM ~ compSUVR + AGE', data=df_filtered).fit()

    # Create a dataframe for p-values and t-values
    for r in range (1, 2): 
        arr = [
            model1a.pvalues[r], 
            model1b.pvalues[r], 
            model2a.pvalues[r], 
            model2b.pvalues[r]
        ]
        arr1 = [
            model1a.tvalues[r], 
            model1b.tvalues[r], 
            model2a.tvalues[r], 
            model2b.tvalues[r]
        ]
        rppp = pd.DataFrame(list(zip(arr, arr1)), columns =['P-value', 'T-value']).T 
        rppp['Amyloid_s_th'] = "NaN"
        rppp['TotalEnergy_GM'] = rppp[0]
        rppp['TotalEnergy_WM'] = rppp[1]
        rppp['IDM_GM'] = rppp[2]
        rppp['IDM_WM'] = rppp[3]
        
        # Rename columns
        nig = rppp.drop(columns=[0, 1, 2, 3, 'Amyloid_s_th'])
        row_names = {0: 'Negative_Mean', 1: 'Positive_Mean', 0: 'Negative_SD', 1: 'Positive_SD'}
        final = nig.rename(index=row_names)
        dm = pd.DataFrame(final)
        j = dm.transpose()
        cols = pd.Series(j.columns)
        for dup in j.columns[j.columns.duplicated(keep=False)]:
            cols[j.columns.get_loc(dup)] = ([dup + '.' + str(d_idx) 
                                         if d_idx != 0 
                                         else dup 
                                         for d_idx in range(j.columns.get_loc(dup).sum())]
                                        )
        j.columns = cols
        j.rename(columns={'Negative_SD': "Negative_Mean", 'Positive_SD': "Positive_Mean", 
                          'Negative_SD.1': "Negative_SD", 'Positive_SD.1': "Positive_SD"}, inplace=True)
        
        # Display results
        display(j)
        
        # Save statistical results
        j.to_csv(output_path1, index=True, float_format='%g')

    # Save combined data
    df_combined.to_csv(output_path10, index=False, float_format='%g')

    # Save filtered data
    df_filtered.to_csv(output_path11, index=False, float_format='%g')

# Process data for both x values
for x in [31, 32]:
    process_data(x)

print("Processing complete!")
