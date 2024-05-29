import nibabel as nib
import numpy as np
from skimage.feature import local_binary_pattern
from scipy.stats import skew, kurtosis, moment, iqr
import os
import csv
import glob

def compute_lbp(image_slice, radius=1, n_points=8, method='uniform'):
    """
    Compute LBP for a given image slice.

    Parameters:
    - image_slice: 2D ndarray, the image slice to compute LBP on.
    - radius: int, radius of the circle (default=1).
    - n_points: int, number of points to consider in the circle (default=8).
    - method: str, LBP method to use ('default', 'ror', 'uniform', 'var').

    Returns:
    - lbp_image: 2D ndarray, the LBP transformed image.
    """
    lbp_image = local_binary_pattern(image_slice, n_points, radius, method)
    return lbp_image

def extract_aggregated_features(nifti_file, radius=1, n_points=8, method='uniform'):
    """
    Extract aggregated LBP texture features from a NIfTI (.nii.gz) file.

    Parameters:
    - nifti_file: str, path to the NIfTI file.
    - radius: int, radius of the circle (default=1).
    - n_points: int, number of points to consider in the circle (default=8).
    - method: str, LBP method to use ('default', 'ror', 'uniform', 'var').

    Returns:
    - aggregated_features: dict, dictionary containing aggregated features.
    """
    # Load the NIfTI file
    img = nib.load(nifti_file)
    
    # Get the image data as a NumPy array
    data = img.get_fdata()
    
    # Initialize lists to store feature values for each slice
    means, variances, skewnesses, kurtoses, total_sums, medians, std_devs, iqrs, third_moments, fourth_moments = [], [], [], [], [], [], [], [], [], []

    # Process each slice in the 3D volume
    for slice_index in range(data.shape[2]):
        image_slice = data[:, :, slice_index]
        
        # Compute LBP for the slice
        lbp_image = compute_lbp(image_slice, radius, n_points, method)
        
        # Compute the histogram of LBP
        hist, _ = np.histogram(lbp_image, bins=np.arange(0, n_points + 3), range=(0, n_points + 2))
        
        # Normalize the histogram
        hist = hist.astype("float")
        hist /= hist.sum()
        
        # Compute numeric features from the histogram
        mean = np.mean(hist)
        variance = np.var(hist)
        skewness = skew(hist)
        kurt = kurtosis(hist)
        median = np.median(hist)
        std_dev = np.std(hist)
        interquartile_range = iqr(hist)
        third_moment = moment(hist, moment=3)
        fourth_moment = moment(hist, moment=4)
        
        # Compute the sum of values for the original image slice
        total_sum = np.sum(image_slice)
        
        # Append features to the lists
        means.append(mean)
        variances.append(variance)
        skewnesses.append(skewness)
        kurtoses.append(kurt)
        medians.append(median)
        std_devs.append(std_dev)
        iqrs.append(interquartile_range)
        third_moments.append(third_moment)
        fourth_moments.append(fourth_moment)
        total_sums.append(total_sum)
    
    # Aggregate features across all slices
    aggregated_features = {
        'mean_of_means': np.mean(means),
        'mean_of_variances': np.mean(variances),
        'mean_of_skewnesses': np.mean(skewnesses),
        'mean_of_kurtoses': np.mean(kurtoses),
        'mean_of_medians': np.mean(medians),
        'mean_of_std_devs': np.mean(std_devs),
        'mean_of_iqrs': np.mean(iqrs),
        'mean_of_third_moments': np.mean(third_moments),
        'mean_of_fourth_moments': np.mean(fourth_moments),
        'total_sum': np.sum(total_sums)
    }
    
    return aggregated_features

# Define input and output directories
#image_folder = "/Users/demoranky/documents/check_pro3_1"  # Replace with your path
image_folder = "/Users/demoranky/documents/check_pro3"  # Replace with your path
output_folder = "/Users/demoranky/documents/water_LBP"  # Replace with your path
os.makedirs(output_folder, exist_ok=True)

# List of x values to iterate over
#x_values = [31, 47, 100, 102, 104, 106, 108, 112, 114, 116, 118, 120, 122, 124, 128, 132, 134, 136, 138, 140, 142]  # Add more x values as needed
x_values =[144, 146, 148, 150, 152, 154, 156, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 190, 192, 194, 196, 198, 200, 202, 204, 206]  # Add more x values as needed
# Iterate over each x value
for x in x_values:
    # Find all NIfTI files matching the pattern
    nifti_files = glob.glob(os.path.join(image_folder, f'*_labelWM_{x}_.nii.gz'))
    
    # Initialize list to store features for the current x value
    features_for_x = []
    
    # Loop through each found NIfTI file and extract features
    for nifti_file in nifti_files:
        # Extract the label identifier from the file name
        file_name = os.path.basename(nifti_file)
        
        aggregated_features = extract_aggregated_features(nifti_file)
        aggregated_features['file_name'] = file_name  # Add file name to features
        
        features_for_x.append(aggregated_features)
    
    # Save features for the current x value to a CSV file
    csv_file = os.path.join(output_folder, f'WM_{x}.csv')
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        header = ['file_name'] + list(features_for_x[0].keys())
        writer.writerow(header)
        # Write data rows
        for features in features_for_x:
            writer.writerow([features['file_name']] + list(features.values()))
    
    print(f"Aggregated features for x={x} saved to {csv_file}")

print("All aggregated features saved.")








import nibabel as nib
import numpy as np
from skimage.feature import local_binary_pattern
from scipy.stats import skew, kurtosis, moment, iqr
import os
import csv
import glob

def compute_lbp(image_slice, radius=1, n_points=8, method='uniform'):
    """
    Compute LBP for a given image slice.

    Parameters:
    - image_slice: 2D ndarray, the image slice to compute LBP on.
    - radius: int, radius of the circle (default=1).
    - n_points: int, number of points to consider in the circle (default=8).
    - method: str, LBP method to use ('default', 'ror', 'uniform', 'var').

    Returns:
    - lbp_image: 2D ndarray, the LBP transformed image.
    """
    lbp_image = local_binary_pattern(image_slice, n_points, radius, method)
    return lbp_image

def extract_aggregated_features(nifti_file, radius=1, n_points=8, method='uniform'):
    """
    Extract aggregated LBP texture features from a NIfTI (.nii.gz) file.

    Parameters:
    - nifti_file: str, path to the NIfTI file.
    - radius: int, radius of the circle (default=1).
    - n_points: int, number of points to consider in the circle (default=8).
    - method: str, LBP method to use ('default', 'ror', 'uniform', 'var').

    Returns:
    - aggregated_features: dict, dictionary containing aggregated features.
    """
    # Load the NIfTI file
    img = nib.load(nifti_file)
    
    # Get the image data as a NumPy array
    data = img.get_fdata()
    
    # Initialize lists to store feature values for each slice
    means, variances, skewnesses, kurtoses, total_sums, medians, std_devs, iqrs, third_moments, fourth_moments = [], [], [], [], [], [], [], [], [], []

    # Process each slice in the 3D volume
    for slice_index in range(data.shape[2]):
        image_slice = data[:, :, slice_index]
        
        # Compute LBP for the slice
        lbp_image = compute_lbp(image_slice, radius, n_points, method)
        
        # Compute the histogram of LBP
        hist, _ = np.histogram(lbp_image, bins=np.arange(0, n_points + 3), range=(0, n_points + 2))
        
        # Normalize the histogram
        hist = hist.astype("float")
        hist /= hist.sum()
        
        # Compute numeric features from the histogram
        mean = np.mean(hist)
        variance = np.var(hist)
        skewness = skew(hist)
        kurt = kurtosis(hist)
        median = np.median(hist)
        std_dev = np.std(hist)
        interquartile_range = iqr(hist)
        third_moment = moment(hist, moment=3)
        fourth_moment = moment(hist, moment=4)
        
        # Compute the sum of values for the original image slice
        total_sum = np.sum(image_slice)
        
        # Append features to the lists
        means.append(mean)
        variances.append(variance)
        skewnesses.append(skewness)
        kurtoses.append(kurt)
        medians.append(median)
        std_devs.append(std_dev)
        iqrs.append(interquartile_range)
        third_moments.append(third_moment)
        fourth_moments.append(fourth_moment)
        total_sums.append(total_sum)
    
    # Aggregate features across all slices
    aggregated_features = {
        'mean_of_means': np.mean(means),
        'mean_of_variances': np.mean(variances),
        'mean_of_skewnesses': np.mean(skewnesses),
        'mean_of_kurtoses': np.mean(kurtoses),
        'mean_of_medians': np.mean(medians),
        'mean_of_std_devs': np.mean(std_devs),
        'mean_of_iqrs': np.mean(iqrs),
        'mean_of_third_moments': np.mean(third_moments),
        'mean_of_fourth_moments': np.mean(fourth_moments),
        'total_sum': np.sum(total_sums)
    }
    
    return aggregated_features

# Define input and output directories
#image_folder = "/Users/demoranky/documents/check_pro3_1"  # Replace with your path
image_folder = "/Users/demoranky/documents/check_pro3"  # Replace with your path
output_folder = "/Users/demoranky/documents/water_LBP"  # Replace with your path
os.makedirs(output_folder, exist_ok=True)

# List of x values to iterate over
#x_values = [31, 47, 100, 102, 104, 106, 108, 112, 114, 116, 118, 120, 122, 124, 128, 132, 134, 136, 138, 140, 142]  # Add more x values as needed
x_values =[144, 146, 148, 150, 152, 154, 156, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 190, 192, 194, 196, 198, 200, 202, 204, 206]  # Add more x values as needed
# Iterate over each x value
# Iterate over each x value
for x in x_values:
    # Find all NIfTI files matching the pattern
    nifti_files = glob.glob(os.path.join(image_folder, f'*label_{x}_.nii.gz'))
    
    # Initialize list to store features for the current x value
    features_for_x = []
    
    # Loop through each found NIfTI file and extract features
    for nifti_file in nifti_files:
        # Extract the label identifier from the file name
        file_name = os.path.basename(nifti_file)
        
        aggregated_features = extract_aggregated_features(nifti_file)
        aggregated_features['file_name'] = file_name  # Add file name to features
        
        features_for_x.append(aggregated_features)
    
    # Save features for the current x value to a CSV file
    csv_file = os.path.join(output_folder, f'GM_{x}.csv')
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        header = ['file_name'] + list(features_for_x[0].keys())
        writer.writerow(header)
        # Write data rows
        for features in features_for_x:
            writer.writerow([features['file_name']] + list(features.values()))
    
    print(f"Aggregated features for x={x} saved to {csv_file}")

print("All aggregated features saved.")
