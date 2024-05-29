import pandas as pd
import numpy as np

def calculate_ratio(input_csv_path, output_csv_path, column_pairs):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv_path)
    
    # Calculate the ratio for each pair of columns
    for column1, column2 in column_pairs:
        # Ensure that the specified columns are present in the DataFrame
        if column1 not in df.columns or column2 not in df.columns:
            raise ValueError(f"The required columns '{column1}' and/or '{column2}' are not present in the CSV file.")
        
        # Calculate the ratio of column1 to column2
        ratio_column_name_1 = f"ratio_{column1}_{column2}"
        df[ratio_column_name_1] = df[column1] / df[column2]
        
        # Calculate the ratio of column2 to column1
        ratio_column_name_2 = f"ratio_{column2}_{column1}"
        df[ratio_column_name_2] = df[column2] / df[column1]
        
        # Replace inf values with NaN
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        
        # Drop rows with NaN values in the specified columns or their ratios
        df.dropna(subset=[column1, column2, ratio_column_name_1, ratio_column_name_2], inplace=True)
        
        # Drop rows with zero values in column1 or column2
        df = df[(df[column1] != 0) & (df[column2] != 0)]
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_csv_path, index=False)
    
    print(f"Ratios for columns {column_pairs} calculated and saved to {output_csv_path}")

# List of x values
x_values = [
    31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 
    114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 
    133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 
    148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 
    165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 
    181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 
    200, 201, 202, 203, 204, 205, 206, 207
]

# Pairs of columns for which to calculate the ratio
column_pairs = [
    ("Medians_WM", "Medians_GM"),
    ("Iqrs_WM", "Iqrs_GM")
]

# Loop over each x value and perform the ratio calculation
for x in x_values:
    input_csv_path = f"/Users/demoranky/documents/water_LBP/final_{x}_GM_WM.csv"
    output_csv_path = f"/Users/demoranky/documents/water_LBP/final_{x}_GM_WM_with_ratio.csv"
    
    try:
        calculate_ratio(input_csv_path, output_csv_path, column_pairs)
    except Exception as e:
        print(f"An error occurred for x = {x}: {e}")
