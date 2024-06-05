import pandas as pd
import matplotlib.pyplot as plt

# Define file path (replace with your actual CSV file path)
file_path = "/Users/demoranky/documents/water_LBP/final_202_GM_WM.csv"

# Read data from CSV file
data = pd.read_csv(file_path)

# Ensure only two groups and numeric value columns (modify if needed)
data = data[data['Amyloid_s_th'].isin(["Negative", "Positive"])]
data['Iqrs_WM'] = pd.to_numeric(data['Iqrs_WM'], errors='coerce')
data['Iqrs_GM'] = pd.to_numeric(data['Iqrs_GM'], errors='coerce')

# Check if value columns are numeric
if not data[['Iqrs_WM', 'Iqrs_GM']].select_dtypes(include=['number']).columns.tolist():
    raise ValueError("Error: 'Iqrs_WM' and 'Iqrs_GM' columns must be numeric for histogram.")

# Plot histograms
plt.figure(figsize=(10, 5))

# Define features
features = ["Iqrs_WM", "Iqrs_GM"]

for i, feature in enumerate(features, 1):
    plt.subplot(1, 2, i)
    plt.hist(data[data['Amyloid_s_th'] == 'Negative'][feature], color='blue', alpha=0.5, label='Negative')
    plt.hist(data[data['Amyloid_s_th'] == 'Positive'][feature], color='red', alpha=0.5, label='Positive')
    plt.xlabel(f'{feature} Value')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {feature}')
    plt.legend()

plt.tight_layout()
plt.show()
