import pandas as pd
from scipy import stats
from scipy.stats import ttest_ind_from_stats
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols


# Iterate over the values in z to process CSV files for each value
z_values = [31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 133, 134, 135, 136, 137, 138, 139,140, 141,142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207]

for z in z_values:
    # Read the CSV files
    dpp = pd.read_csv(f'/Users/demoranky/documents/water/{z}_GM.csv')
    dpp["Image_Root"] = dpp["Image_Root"].str.replace(f'_label_{z}_.nii', '', regex=True)
    dpp = dpp.sort_values("Image_Root")
    dpp['IDM_GM'] = dpp['Inverse different moment']
    dpp['TotalEnergy_GM'] = dpp['Total energy']
    dpp['entropy_GM'] = dpp['entropy']
    dpp['kurtosis_GM'] = dpp['kurtosis']
    dpp['Sum_var_GM'] = dpp['sum_variance']
    dpp['Skew_GM'] = dpp['skewness']
    dpp['Sum_Aver_GM'] = dpp['sum_average']
    dpp['contrast_GM'] = dpp['contrast']
    dpp_gm = dpp[["IDM_GM", "TotalEnergy_GM", "entropy_GM", "kurtosis_GM", "Sum_var_GM", "Skew_GM", "Sum_Aver_GM", "contrast_GM"]]

    dpp1 = pd.read_csv(f'/Users/demoranky/documents/water/{z}_WM.csv')
    dpp1["Image_Root"] = dpp1["Image_Root"].str.replace(f'_labelWM_{z}_.nii', '', regex=True)
    dpp1 = dpp1.sort_values("Image_Root")
    dpp1['IDM_WM'] = dpp1['Inverse different moment']
    dpp1['TotalEnergy_WM'] = dpp1['Total energy']
    dpp1['entropy_WM'] = dpp1['entropy']
    dpp1['kurtosis_WM'] = dpp1['kurtosis']
    dpp1['Sum_var_WM'] = dpp1['sum_variance']
    dpp1['Skew_WM'] = dpp1['skewness']
    dpp1['Sum_Aver_WM'] = dpp1['sum_average']
    dpp1['contrast_WM'] = dpp1['contrast']
    dpp_wm = dpp1[["IDM_WM", "TotalEnergy_WM", "entropy_WM", "kurtosis_WM", "Sum_var_WM", "Skew_WM", "Sum_Aver_WM", "contrast_WM", "Image_Root"]]

    # Merge dpp_gm and dpp_wm
    dfr2 = pd.concat([dpp_wm, dpp_gm], axis=1)
    
    # Read the second CSV file
    df12 = pd.read_csv('/Users/demoranky/documents/cova_abc_new.csv')

    # Merge dfr2 and df1 on index
    #merged_df = pd.merge(df12, dfr2, left_index=True, right_index=True, how="inner")
    merged_df = pd.merge(df12, dfr2, on='Image_Root', how='inner')
    merged_df_cleaned = merged_df.dropna()
    out_path5 = f"/Users/demoranky/documents/water/final_{z}_GM_WM.csv"
    merged_df_cleaned.to_csv(out_path5, index=False)
    #display(merged_df_cleaned)