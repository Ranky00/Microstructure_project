import nibabel as nib
import numpy as np
from skimage.feature import local_binary_pattern
from scipy.stats import skew, kurtosis, moment, iqr
import os
import csv
import glob

def compute_lbp(image_slice, radius=1, n_points=8, method='uniform'):
    lbp_image = local_binary_pattern(image_slice, n_points, radius, method)
    return lbp_image

def extract_aggregated_features(nifti_file, radius=1, n_points=8, method='uniform'):
    img = nib.load(nifti_file)
    data = img.get_fdata()
    
    means, variances, skewnesses, kurtoses, medians, std_devs, iqrs, third_moments, fourth_moments, total_sums = [], [], [], [], [], [], [], [], [], []

    for slice_index in range(data.shape[2]):
        image_slice = data[:, :, slice_index]
        lbp_image = compute_lbp(image_slice, radius, n_points, method)
        hist, _ = np.histogram(lbp_image, bins=np.arange(0, n_points + 3), range=(0, n_points + 2))
        
        hist = hist.astype("float")
        hist /= hist.sum()
        
        means.append(np.mean(hist))
        variances.append(np.var(hist))
        skewnesses.append(skew(hist))
        kurtoses.append(kurtosis(hist))
        medians.append(np.median(hist))
        std_devs.append(np.std(hist))
        iqrs.append(iqr(hist))
        third_moments.append(moment(hist, moment=3))
        fourth_moments.append(moment(hist, moment=4))
        total_sums.append(np.sum(image_slice))
    
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

#image_folder = "/Users/demoranky/documents/check_pro1"
#image_folder = "/Users/demoranky/documents/check_pro2"
#image_folder = "/Users/demoranky/documents/check_pro1/testingE"
image_folder = "/Users/demoranky/documents/check_pro1/testingE/WA1"
output_folder = "/Users/demoranky/documents/water_LBP"
os.makedirs(output_folder, exist_ok=True)


#x_values = [101, 103, 105, 107, 109, 113, 115, 117, 119, 121, 123, 125, 129, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 191]  # Add more x values as needed
#x_values = [193, 195, 197, 199, 201, 203, 205, 207]  # Add more x values as needed
#x_values = [32]  # Add more x values as needed
x_values = [48]  # Add more x values as needed
for x in x_values:
    nifti_files = glob.glob(os.path.join(image_folder, f'*_labelWM_{x}_.nii.gz'))
    features_for_x = []
    
    for nifti_file in nifti_files:
        file_name = os.path.basename(nifti_file)
        aggregated_features = extract_aggregated_features(nifti_file)
        aggregated_features['file_name'] = file_name
        features_for_x.append(aggregated_features)
    
    csv_file = os.path.join(output_folder, f'WM_{x}.csv')
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['file_name'] + list(features_for_x[0].keys()))
        writer.writeheader()
        for features in features_for_x:
            writer.writerow(features)
    
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
    lbp_image = local_binary_pattern(image_slice, n_points, radius, method)
    return lbp_image

def extract_aggregated_features(nifti_file, radius=1, n_points=8, method='uniform'):
    img = nib.load(nifti_file)
    data = img.get_fdata()
    
    means, variances, skewnesses, kurtoses, medians, std_devs, iqrs, third_moments, fourth_moments, total_sums = [], [], [], [], [], [], [], [], [], []

    for slice_index in range(data.shape[2]):
        image_slice = data[:, :, slice_index]
        lbp_image = compute_lbp(image_slice, radius, n_points, method)
        hist, _ = np.histogram(lbp_image, bins=np.arange(0, n_points + 3), range=(0, n_points + 2))
        
        hist = hist.astype("float")
        hist /= hist.sum()
        
        means.append(np.mean(hist))
        variances.append(np.var(hist))
        skewnesses.append(skew(hist))
        kurtoses.append(kurtosis(hist))
        medians.append(np.median(hist))
        std_devs.append(np.std(hist))
        iqrs.append(iqr(hist))
        third_moments.append(moment(hist, moment=3))
        fourth_moments.append(moment(hist, moment=4))
        total_sums.append(np.sum(image_slice))
    
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
#image_folder = "/Users/demoranky/documents/check_pro1"
#image_folder = "/Users/demoranky/documents/check_pro2"
#image_folder = "/Users/demoranky/documents/check_pro1/testingE"
image_folder = "/Users/demoranky/documents/check_pro1/testingE/WA1"
output_folder = "/Users/demoranky/documents/water_LBP"
os.makedirs(output_folder, exist_ok=True)

#x_values = [101, 103, 105, 107, 109, 113, 115, 117, 119, 121, 123, 125, 129, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 191]  # Add more x values as needed
#x_values = [193, 195, 197, 199, 201, 203, 205, 207]  # Add more x values as needed
#x_values = [32]  # Add more x values as needed
x_values = [48]  # Add more x values as needed
for x in x_values:
    nifti_files = glob.glob(os.path.join(image_folder, f'*label_{x}_.nii.gz'))
    features_for_x = []
    
    for nifti_file in nifti_files:
        file_name = os.path.basename(nifti_file)
        aggregated_features = extract_aggregated_features(nifti_file)
        aggregated_features['file_name'] = file_name
        features_for_x.append(aggregated_features)
    
    csv_file = os.path.join(output_folder, f'GM_{x}.csv')
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['file_name'] + list(features_for_x[0].keys()))
        writer.writeheader()
        for features in features_for_x:
            writer.writerow(features)
    
    print(f"Aggregated features for x={x} saved to {csv_file}")

print("All aggregated features saved.")

