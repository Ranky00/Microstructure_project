import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

def perform_pca(input_csv_path, output_csv_path, selected_features, n_components):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv_path)
    
    # Ensure that the specified features are present in the DataFrame
    missing_features = [feature for feature in selected_features if feature not in df.columns]
    if missing_features:
        raise ValueError(f"The required features are not present in the CSV file: {missing_features}")
    
    # Extract the selected features
    features = df[selected_features]
    
    # Standardize the features
    scaler = StandardScaler()
    standardized_features = scaler.fit_transform(features)
    
    # Perform PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(standardized_features)
    
    # Take the absolute values of the principal components
    principal_components = np.abs(principal_components)
    
    # Create a DataFrame for the principal components
    principal_df = pd.DataFrame(data=principal_components, columns=[f'PC{i+1}' for i in range(n_components)])
    
    # Concatenate the principal components with the original DataFrame (excluding the selected features)
    final_df = pd.concat([df.drop(columns=selected_features), principal_df], axis=1)
    
    # Save the resulting DataFrame to a new CSV file
    final_df.to_csv(output_csv_path, index=False)
    
    print(f"PCA applied to features {selected_features} and saved to {output_csv_path}")

# List of x values
x_values = [31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 
    114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 
    133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 
    148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 
    165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 
    181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 
    200, 201, 202, 203, 204, 205, 206, 207]

# Selected features and number of components
selected_features = ["mean_of_means", "mean_of_variances", "mean_of_skewnesses", "mean_of_kurtoses", "mean_of_medians", "mean_of_std_devs", "mean_of_iqrs", "mean_of_third_moments", "mean_of_fourth_moments", "total_sum"]
n_components = 2  # Number of principal components to keep

# Iterate over each x value and perform PCA
for x in x_values:
    input_csv_path = f"/Users/demoranky/documents/water_LBP/WM_{x}.csv"
    output_csv_path = f"/Users/demoranky/documents/water_LBP/selected_feature_{x}_WM.csv"
    
    perform_pca(input_csv_path, output_csv_path, selected_features, n_components)
