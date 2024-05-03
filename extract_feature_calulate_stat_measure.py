import os
import pandas as pd
import SimpleITK as sitk
from radiomics import featureextractor
from scipy.stats import ttest_ind_from_stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

def extract_radiomics_features(input_folder_mask, input_folder_image, output_csv):

    # Initialize feature extractor
    extractor = featureextractor.RadiomicsFeatureExtractor()

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

def extract_radiomics_features_wm(input_folder_mask, input_folder_image, output_csv):

    # Initialize feature extractor
    extractor = featureextractor.RadiomicsFeatureExtractor()

    # List to store dataframes
    Ade_list2 = []

    # Iterate through files in both input folders simultaneously
    for file_mask, file_image in zip(os.listdir(input_folder_mask), os.listdir(input_folder_image)):
        if file_mask.endswith("nii.gz") and file_image.endswith("nii.gz"):
            image1 = sitk.ReadImage(os.path.join(input_folder_mask, file_mask))##mask 
            image2 = sitk.ReadImage(os.path.join(input_folder_image, file_image))##Image
            featureVector2 = extractor.execute(image1, image2, 1)
            Ade2 = pd.DataFrame([featureVector2])
            Ade_list2.append(Ade2)

    # Concatenate all dataframes in the list
    if Ade_list2:
        df2 = pd.concat(Ade_list2)
        df2.to_csv(output_csv, index=True)
    else:
        print("No matching files found in the input folders.")

# Extract GM features
extract_radiomics_features('location_of_input_folder_mask', 'location_of_input_folder_image', 'Location_of_output_csv.csv')

# Extract WM features
extract_radiomics_features_wm('location_of_input_folder_mask1', 'location_of_input_folder_image1', 'location_of_output_csv1.csv')

# Read and merge features of df1 in the saved location
dpp=pd.read_csv('/Users/demoranky/documents/31_GM_fresh.csv')
dpp['IDM_GM']=dpp['original_Inverse_difference_moment']
dpp['TotalEnergy_GM']=dpp['original_firstorder_TotalEnergy']
dpp['TotalEnergy_GM'] = dpp['TotalEnergy_GM'].abs()
dpp['IDM_GM'] = dpp['IDM_GM'].abs()
dpp_gm=dpp[["IDM_GM","TotalEnergy_GM"]]

# Read and merge features of df2 in the saved location
dpp1=pd.read_csv('/Users/demoranky/documents/ADNI_new_extract/31_WM_fresh.csv')
dpp1['IDM_WM']=dpp1['original_Inverse_difference_moment']
dpp1['TotalEnergy_WM']=dpp1['original_firstorder_TotalEnergy']
dpp1['TotalEnergy_WM'] = dpp1['TotalEnergy_WM'].abs()
dpp1['IDM_WM'] = dpp1['IDM_WM'].abs()
                    
dpp_wm=dpp1[["IDM_WM","TotalEnergy_WM"]]
             
dfr2=pd.concat([dpp_wm, dpp_gm], axis=1)
             
toy=pd.read_csv('/Users/demoranky/documents/lovad_ADNI.csv')             
dfr3=pd.concat([dfr2, toy], axis=1)

df1=pd.read_csv('/Users/demoranky/documents/Cova23.csv')
df3= pd.merge(dfr3, df1, on=['Brain_ID'], how='inner')

total_merge = df3.merge(df1, on='Brain_ID', how='outer', indicator=True)

R3 = total_merge[total_merge['_merge']=='right_only']
R3.rename(columns={'Amyloid_s_th_y':'Amyloid_s_th', 'AGE_y':'AGE'}, inplace=True)
df4=R3[["Brain_ID","Amyloid_s_th","AGE"]] 
df4=df4.reset_index(drop=True)
df41=dfr2[["IDM_WM", "IDM_GM", "TotalEnergy_WM", "TotalEnergy_GM"]]
df41=df41.reset_index(drop=True)

df6=pd.concat([df41, df3], axis=0, join='outer')
df6=df6.drop(['RID', 'Dx','Brain_ID_same'], axis=1)
df6=df6.sort_values("Amyloid_s_th")
out_path5 = "/Users/demoranky/documents/ADNI_new_extract/final_31_GM_WM_used.csv"
df6.to_csv(out_path5, index=False)

###Calculate the mean and SD. Be careful, change the "Amyloid_s_th" to whatever you are grouping with
grouped_mean = df1.groupby('Amyloid_s_th')[['TotalEnergy_GM','TotalEnergy_WM','IDM_GM','IDM_WM']].mean().reset_index().round(2)
grouped_sd = df1.groupby('Amyloid_s_th')[['TotalEnergy_GM','TotalEnergy_WM','IDM_GM','IDM_WM']].std().reset_index().round(2)

###Concatenate the mean and SD so they appear in the same frame
frames = [grouped_mean, grouped_sd]
result = pd.concat(frames)

## create a model for the grey and white matter for both total energy and IDM
model1a = ols('TotalEnergy_GM ~ Amyloid_s_th + AGE ', data=df1).fit() 
model1b = ols('TotalEnergy_WM ~ Amyloid_s_th + AGE', data=df1).fit()
model2a= ols('IDM_GM ~ Amyloid_s_th + AGE', data=df1).fit()
model2b= ols('IDM_WM ~ Amyloid_s_th + AGE', data=df1).fit()

#create an array of the p-value and t-values so they fit in the print position of the display table. 
for r in range (1, 2): 
    arr=[model1a.pvalues[r],model1b.pvalues[r],model2a.pvalues[r],model2b.pvalues[r]]
    arr1=[model1a.tvalues[r],model1b.tvalues[r],model2a.tvalues[r],model2b.tvalues[r]]
    rppp= pd.DataFrame(list(zip(arr, arr1)), columns =['P-value', 'T-value']).T 
    rppp['Amyloid_s_th']="NaN";rppp['TotalEnergy_GM']=rppp[0];rppp['TotalEnergy_WM']=rppp[1];rppp['IDM_GM']=rppp[2];rppp['IDM_WM']=rppp[3]

    ##concatenate arrays and the results from the mean and SD.
    frames2 = [result, rppp]
    result2 = pd.concat(frames2)

    ### Show the columns and rows with the requiresd columns and transpose the displays
    nig=result2.drop(columns=[0,1,2,3, 'Amyloid_s_th'])
    row_names ={0:'Negative_Mean',1:'Positive_Mean',0:'Negative_SD',1:'Positive_SD'}
    final=nig.rename(index = row_names)
    dm = pd.DataFrame(final)
    j=dm.transpose()
    cols=pd.Series(j.columns)
    for dup in j.columns[j.columns.duplicated(keep=False)]:
        cols[j.columns.get_loc(dup)] = ([dup + '.' + str(d_idx) 
                                     if d_idx != 0 
                                     else dup 
                                     for d_idx in range(j.columns.get_loc(dup).sum())]
                                    )
    j.columns = cols
    j.rename(columns={'Negative_SD': "Negative_Mean",'Positive_SD': "Positive_Mean",'Negative_SD.1': "Negative_SD",'Positive_SD.1': "Positive_SD"}, inplace = True)
    display(j)

# Round the p-values and t-values to 4 decimal places
j['P-value'] = j['P-value'].apply(lambda x: round(x, 4))  
j['T-value'] = j['T-value'].apply(lambda x: round(x, 4)) 
#out_path8 = "/Users/demoranky/documents/ADNI_new_extract/final_31_GM_WM_LM.csv"
#j.to_csv(out_path8, index=False)