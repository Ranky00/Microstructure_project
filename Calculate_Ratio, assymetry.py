import pandas as pd
import numpy as np

x = [31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 133, 134, 135, 136, 137, 138, 139,140, 141,142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207]

for value in x:
    # Load the CSV file into a DataFrame
    csv_file_path = f"/Users/demoranky/documents/water/final_{value}_GM_WM.csv"
    df = pd.read_csv(csv_file_path)

    # Define column pairs
    column_pairs = [
        ('IDM_WM', 'IDM_GM'),
        ('TotalEnergy_WM', 'TotalEnergy_GM'),
        ('entropy_WM', 'entropy_GM'),
        ('kurtosis_WM', 'kurtosis_GM'),
        ('Sum_var_WM', 'Sum_var_GM'),
        ('Skew_WM', 'Skew_GM'),
        ('Sum_Aver_WM', 'Sum_Aver_GM'),
        ('contrast_WM', 'contrast_GM'),
        # Add more column pairs as needed
    ]

    # Calculate metrics for each column pair
    for col_A, col_B in column_pairs:
        column_A = df[col_A]
        column_B = df[col_B]

        # Calculate asymmetry index
        asymmetry_index = abs(column_A - column_B)

        # Calculate symmetry index
        symmetry_index = (column_A + column_B) / 2

        # Calculate difference
        difference = np.abs(column_A - column_B)

        # Calculate ratio (assuming non-zero denominator)
        ratio = column_A / column_B

        # Add the calculated metrics as new columns to the DataFrame
        df[f'Asymmetry_Index_{col_A}_{col_B}'] = asymmetry_index
        df[f'Symmetry_Index_{col_A}_{col_B}'] = symmetry_index
        df[f'Difference_{col_A}_{col_B}'] = difference
        df[f'Ratio_{col_A}_{col_B}'] = ratio

    # Overwrite the original CSV file with the updated DataFrame
    df.to_csv(csv_file_path, index=False)

    print(f"Calculated metrics added to the original CSV file: {csv_file_path}")
