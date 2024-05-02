import os
from radiomics import featureextractor
import SimpleITK as sitk
import pandas as pd

def extract_radiomics_features(input_folder_mask, input_folder_image, output_csv):

    # List to store dataframes
    Ade_list1 = []

    # Iterate through files in both input folders simultaneously
    for file_mask, file_image in zip(os.listdir(input_folder_mask), os.listdir(input_folder_image)):
        if file_mask.endswith("nii.gz") and file_image.endswith("nii.gz"):
            image1 = sitk.ReadImage(os.path.join(input_folder_mask, file_mask))##mask 
            image2 = sitk.ReadImage(os.path.join(input_folder_image, file_image))##Image
            featureVector1 = extractor.execute(image1, image2, 1)
            Ade1 = pd.DataFrame([featureVector1])
            Ade_list1.append(Ade1)

    # Concatenate all dataframes in the list
    if Ade_list1:
        df1 = pd.concat(Ade_list1)
        df1.to_csv(output_csv, index=True)
    else:
        print("No matching files found in the input folders.")

extract_radiomics_features('location_of_mask', 'location_of_image', 'location_of_output_csv.csv')