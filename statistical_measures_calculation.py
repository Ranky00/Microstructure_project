import pandas as pd
from statsmodels.formula.api import ols
from scipy.stats import ttest_ind_from_stats

def read_data(file_path):
    df = pd.read_csv(file_path)
    return df

def calculate_mean_sd(df):
    grouped_mean = df.groupby('Amyloid_s_th')[['TotalEnergy_GM','TotalEnergy_WM','IDM_GM','IDM_WM']].mean().reset_index().round(2)
    grouped_sd = df.groupby('Amyloid_s_th')[['TotalEnergy_GM','TotalEnergy_WM','IDM_GM','IDM_WM']].std().reset_index().round(2)
    result = pd.concat([grouped_mean, grouped_sd], ignore_index=True)
    return result

def create_models(df):
    model1a = ols('TotalEnergy_GM ~ Amyloid_s_th + AGE', data=df).fit() 
    model1b = ols('TotalEnergy_WM ~ Amyloid_s_th + AGE', data=df).fit()
    model2a = ols('IDM_GM ~ Amyloid_s_th + AGE', data=df).fit()
    model2b = ols('IDM_WM ~ Amyloid_s_th + AGE', data=df).fit()
    return model1a, model1b, model2a, model2b

def calculate_pvalues_tvalues(models):
    p_values = []
    t_values = []
    for model in models:
        p_values.append(model.pvalues[1])
        t_values.append(model.tvalues[1])
    return p_values, t_values

def display_results(mean_sd, p_values, t_values):
    result_df = mean_sd.copy()
    result_df = result_df.drop(columns=['Amyloid_s_th']).T
    result_df.rename(columns={0: 'Negative_Mean', 1: 'Positive_Mean', 2: 'Negative_SD', 3: 'Positive_SD'}, inplace=True)
    result_df['P-value'] = p_values
    result_df['T-value'] = t_values
    display(result_df)

# Main function
def main(file_path):
    df = read_data(file_path)
    mean_sd = calculate_mean_sd(df)
    models = create_models(df)
    p_values, t_values = calculate_pvalues_tvalues(models)
    display_results(mean_sd, p_values, t_values)

# Execute the main function
if __name__ == "__main__":
    file_path = '/150_IDM_TE.csv'
    main(file_path)
