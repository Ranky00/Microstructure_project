pobj <- read_csv('/Users/demoranky/documents/okay_obj222.csv')
WM_Obj_d = glm(Mean1 ~WM_Obj_d + Education + Gender, family = "gaussian", data =pobj)
plot(WM_Obj_d.pit)

summary(WM_Obj_d)
# Family = "gaussian" to train a linear regression model
lrModel <- glm(Mean1 ~ WM_Obj_d, data = pobj, family = "gaussian")

# Print a summary of the trained model
summary(lrModel)

attach(pobj)
plot(Mean1 ~WM_Obj_d )


WM_Obj_d.fit =glm(formula = cbind(Mean1) ~ Gender +Education + F_d + WM_Obj_d, family = gaussian,data =pobj) 
summary(WM_Obj_d.fit)
predict(WM_Obj_d.fit, newdata = data.frame(WM_Obj_d = 1))


library(ggplot2)

#create scatter plot
ggplot(pobj, aes(x=Education, y=Gender)) +
  geom_point(size=2)

pj <- read_csv('/Users/demoranky/documents/expt_cog_matlab_small_filtered1.csv')
ggplot(pj, aes(y=WM_Obj_d)) +
  geom_boxplot()




# Read the CSV file
df <- read.csv("/Users/demoranky/documents/untitled folder/Another_ABC/final_31_GM_WM.csv")

# Specify the columns you want to compare and the covariate column
group <- df$Amyloid_s_th
outcome1 <- df$TotalEnergy_WM_power_transformed
outcome2 <- df$TotalEnergy_GM_power_transformed
age <- df$AGE

# Perform GLM with AGE as a covariate for Outcome1
glm_model1 <- glm(outcome1 ~ group + age, family = gaussian(link = "identity"))

# Perform GLM with AGE as a covariate for Outcome2
glm_model2 <- glm(outcome2 ~ group + age, family = gaussian(link = "identity"))

# Extract t-values and p-values for AGE effect
summary_glm1 <- summary(glm_model1)
t_value1 <- summary_glm1$coefficients["age", "t value"]
p_value1 <- summary_glm1$coefficients["age", "Pr(>|t|)"]

summary_glm2 <- summary(glm_model2)
t_value2 <- summary_glm2$coefficients["age", "t value"]
p_value2 <- summary_glm2$coefficients["age", "Pr(>|t|)"]

# Create a data frame for the results
results_df <- data.frame(
  "Outcome Variable" = c("T-value", "P-value"),
  "Outcome 1" = c(t_value1, p_value1),
  "Outcome 2" = c(t_value2, p_value2)
)

# Print the results side by side
print(results_df.T)







# Define the x values
x_values <- c(31, 47, 100, 101)

# Read the CSV file
df <- read.csv("/Users/demoranky/documents/water/final_31_values_GM_WM.csv")

# Specify the group and covariate columns
group <- df$Amyloid_s_th
age <- df$AGE

# Define a list of outcome columns to analyze
outcome_columns <- c("TotalEnergy_WM", "TotalEnergy_GM", "IDM_WM", "IDM_GM")

# Initialize an empty data frame to store results
results_df <- data.frame("Outcome Variable" = c("T-value", "P-value"))

# Loop over each outcome column
for (outcome_col in outcome_columns) {
  
  # Perform GLM with AGE as a covariate for the current outcome column
  glm_model <- glm(df[[outcome_col]] ~ group + age, family = gaussian(link = "identity"))
  
  # Extract t-value and p-value for AGE effect
  summary_glm <- summary(glm_model)
  t_value <- summary_glm$coefficients["age", "t value"]
  p_value <- summary_glm$coefficients["age", "Pr(>|t|)"]
  
  # Add the results to the data frame
  results_df[outcome_col] <- c(t_value, p_value)
}

# Print the results in a tabular format
print(results_df)








# Define the x values
x_values <- c(31, 47, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 133, 134, 135, 136, 137, 138, 139)

# Define a function to perform the GLM analysis for a given x value
perform_glm_analysis <- function(x) {
  # Construct the file path based on the current x value
  file_path <- paste0("/Users/demoranky/documents/water/final_", x, "_GM_WM.csv")
  
  # Check if the file exists
  if (!file.exists(file_path)) {
    stop("File not found: ", file_path)
  }
  
  # Read the CSV file
  df <- read.csv(file_path)
  
  # Specify the group and covariate columns
  group <- df$Amyloid_s_th
  age <- df$AGE
  
  # Define a list of outcome columns to analyze
  outcome_columns <- c("TotalEnergy_WM", "TotalEnergy_GM", "IDM_WM", "IDM_GM")
  
  # Initialize an empty data frame to store results
  results_df <- data.frame("Outcome Variable" = c("T-value", "P-value"))
  
  # Loop over each outcome column
  for (outcome_col in outcome_columns) {
    # Perform GLM with AGE as a covariate for the current outcome column
    glm_model <- glm(df[[outcome_col]] ~ group + age, family = gaussian(link = "identity"))
    
    # Extract t-value and p-value for AGE effect
    summary_glm <- summary(glm_model)
    t_value <- summary_glm$coefficients["age", "t value"]
    p_value <- summary_glm$coefficients["age", "Pr(>|t|)"]
    
    # Add the results to the data frame
    results_df[outcome_col] <- c(t_value, p_value)
  }
  
  # Return the results data frame
  return(results_df)
}

# Initialize a list to store results for all x values
all_results <- list()

# Loop over each x value and perform the analysis
for (x in x_values) {
  results <- perform_glm_analysis(x)
  all_results[[paste0("x_", x)]] <- results
}

# Print the results for each x value
for (x in names(all_results)) {
  cat("Results for x =", x, ":\n")
  print(all_results[[x]])
  cat("\n")
}












# Define the x values
x_values <- c(31, 47, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 133, 134, 135, 136, 137, 138, 139)


# Define a function to perform the GLM analysis for a given x value
perform_glm_analysis <- function(x) {
  # Construct the file path based on the current x value
  file_path <- paste0("/Users/demoranky/documents/water/final_", x, "_GM_WM.csv")
  
  # Check if the file exists
  if (!file.exists(file_path)) {
    stop("File not found: ", file_path)
  }
  
  # Read the CSV file
  df <- read.csv(file_path)
  
  # Specify the group and covariate columns
  group <- df$Amyloid_s_th
  age <- df$AGE
  
  # Define a list of outcome columns to analyze
  outcome_columns <- c("TotalEnergy_WM", "TotalEnergy_GM", "IDM_WM", "IDM_GM")
  
  # Initialize an empty data frame to store results
  results_df <- data.frame("Statistic" = c("Mean", "SD", "T-value", "P-value"))
  
  # Loop over each outcome column
  for (outcome_col in outcome_columns) {
    # Calculate mean and standard deviation for the current outcome column
    mean_value <- mean(df[[outcome_col]], na.rm = TRUE)
    sd_value <- sd(df[[outcome_col]], na.rm = TRUE)
    
    # Perform GLM with AGE as a covariate for the current outcome column
    glm_model <- glm(df[[outcome_col]] ~ group + age, family = gaussian(link = "identity"))
    
    # Extract t-value and p-value for AGE effect
    summary_glm <- summary(glm_model)
    t_value <- summary_glm$coefficients["age", "t value"]
    p_value <- summary_glm$coefficients["age", "Pr(>|t|)"]
    
    # Add the results to the data frame
    results_df[outcome_col] <- c(mean_value, sd_value, t_value, p_value)
  }
  
  # Return the results data frame
  return(results_df)
}

# Initialize a list to store results for all x values
all_results <- list()

# Loop over each x value and perform the analysis
for (x in x_values) {
  results <- perform_glm_analysis(x)
  all_results[[paste0("x_", x)]] <- results
}

# Print the results for each x value
for (x in names(all_results)) {
  cat("Results for x =", x, ":\n")
  print(all_results[[x]])
  cat("\n")
}






# Define the x values
x_values <- c(31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 133, 134, 135, 136, 137, 138, 139,140, 141,142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207)

# Define a function to perform the GLM analysis for a given x value
perform_glm_analysis <- function(x) {
  # Construct the file path based on the current x value
  file_path <- paste0("/Users/demoranky/documents/water/final_", x, "_GM_WM.csv")
  
  # Check if the file exists
  if (!file.exists(file_path)) {
    stop("File not found: ", file_path)
  }
  
  # Read the CSV file
  df <- read.csv(file_path)
  
  # Specify the covariate column
  age <- df$AGE
  
  # Define a list of outcome columns to analyze
  outcome_columns <- c("TotalEnergy_WM", "TotalEnergy_GM", "IDM_WM", "IDM_GM", "entropy_WM","entropy_GM", "kurtosis_WM", "kurtosis_GM", "Sum_var_WM","Sum_var_GM", "Skew_WM","Skew_GM", "Sum_Aver_WM","Sum_Aver_GM", "contrast_WM","contrast_GM")
  
  # Initialize an empty data frame to store results
  results_df <- data.frame("Statistic" = c("Mean_Positive", "SD_Positive", "Mean_Negative", "SD_Negative", "T-value", "P-value"))
  
  # Loop over each outcome column
  for (outcome_col in outcome_columns) {
    # Calculate mean and standard deviation for positive and negative groups
    mean_positive <- mean(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    sd_positive <- sd(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    mean_negative <- mean(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    sd_negative <- sd(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    
    # Perform GLM with AGE as a covariate for the current outcome column
    glm_model <- glm(df[[outcome_col]] ~ df$Amyloid_s_th + age, family = gaussian(link = "identity"))
    
    # Extract t-value and p-value for the Amyloid_s_th effect
    summary_glm <- summary(glm_model)
    t_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "t value"]
    p_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "Pr(>|t|)"]
    
    # Add the results to the data frame
    results_df[outcome_col] <- c(mean_positive, sd_positive, mean_negative, sd_negative, t_value, p_value)
  }
  
  # Return the results data frame
  return(results_df)
}

# Initialize a list to store results for all x values
all_results <- list()

# Loop over each x value and perform the analysis
for (x in x_values) {
  results <- perform_glm_analysis(x)
  all_results[[paste0("x_", x)]] <- results
}

# Print the results for each x value
for (x in names(all_results)) {
  cat("Results for x =", x, ":\n")
  print(all_results[[x]])
  cat("\n")
}






# Define the x values
x_values <- c(31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207)

# Define a function to perform the GLM analysis for a given x value
perform_glm_analysis <- function(x) {
  # Construct the file path based on the current x value
  file_path <- paste0("/Users/demoranky/documents/water/final_", x, "_GM_WM.csv")
  
  # Check if the file exists
  if (!file.exists(file_path)) {
    stop("File not found: ", file_path)
  }
  
  # Read the CSV file
  df <- read.csv(file_path)
  
  # Specify the covariate column
  age <- df$AGE
  
  # Define a list of outcome columns to analyze
  outcome_columns <- c("TotalEnergy_WM", "TotalEnergy_GM", "IDM_WM", "IDM_GM", "entropy_WM","entropy_GM", "kurtosis_WM", "kurtosis_GM", "Sum_var_WM","Sum_var_GM", "Skew_WM","Skew_GM", "Sum_Aver_WM","Sum_Aver_GM", "contrast_WM","contrast_GM")
  
  # Initialize an empty data frame to store results
  results_df <- data.frame("Statistic" = c("Mean_Positive", "SD_Positive", "Mean_Negative", "SD_Negative", "T-value", "P-value"))
  
  # Loop over each outcome column
  for (outcome_col in outcome_columns) {
    # Calculate mean and standard deviation for positive and negative groups
    mean_positive <- mean(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    sd_positive <- sd(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    mean_negative <- mean(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    sd_negative <- sd(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    
    # Perform GLM with AGE as a covariate for the current outcome column
    glm_model <- glm(df[[outcome_col]] ~ df$Amyloid_s_th + age, family = gaussian(link = "identity"))
    
    # Extract t-value and p-value for the Amyloid_s_th effect
    summary_glm <- summary(glm_model)
    t_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "t value"]
    p_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "Pr(>|t|)"]
    
    # Add the results to the data frame
    results_df[outcome_col] <- c(mean_positive, sd_positive, mean_negative, sd_negative, t_value, p_value)
  }
  
  # Add a column for the x value
  results_df$x_value <- x
  
  # Return the results data frame
  return(results_df)
}

# Initialize an empty data frame to store all results
all_results_df <- data.frame()

# Loop over each x value and perform the analysis
for (x in x_values) {
  results_df <- perform_glm_analysis(x)
  all_results_df <- rbind(all_results_df, results_df)
}

# Write all results to a single CSV file
write.csv(all_results_df, "/Users/demoranky/documents/water/all_results.csv", row.names = FALSE)










# Define the x values
x_values <- c(31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 133, 134, 135, 136, 137, 138, 139,140, 141,142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207)

# Define a function to perform the GLM analysis for a given x value
perform_glm_analysis <- function(x) {
  # Construct the file path based on the current x value
  file_path <- paste0("/Users/demoranky/documents/water/final_", x, "_GM_WM.csv")
  
  # Check if the file exists
  if (!file.exists(file_path)) {
    stop("File not found: ", file_path)
  }
  
  # Read the CSV file
  df <- read.csv(file_path)
  
  # Specify the covariate column
  age <- df$AGE
  
  # Define a list of outcome columns to analyze
  outcome_columns <- c("Symmetry_Index_IDM_WM_IDM_GM","Difference_IDM_WM_IDM_GM",	"Ratio_IDM_WM_IDM_GM","Asymmetry_Index_TotalEnergy_WM_TotalEnergy_GM","Symmetry_Index_TotalEnergy_WM_TotalEnergy_GM",	"Difference_TotalEnergy_WM_TotalEnergy_GM",	"Ratio_TotalEnergy_WM_TotalEnergy_GM",	"Asymmetry_Index_entropy_WM_entropy_GM",	"Symmetry_Index_entropy_WM_entropy_GM",	"Difference_entropy_WM_entropy_GM",	"Ratio_entropy_WM_entropy_GM",	"Asymmetry_Index_kurtosis_WM_kurtosis_GM",	"Symmetry_Index_kurtosis_WM_kurtosis_GM",	"Difference_kurtosis_WM_kurtosis_GM",	"Ratio_kurtosis_WM_kurtosis_GM",	"Asymmetry_Index_Sum_var_WM_Sum_var_GM",	"Symmetry_Index_Sum_var_WM_Sum_var_GM",	"Difference_Sum_var_WM_Sum_var_GM",	"Ratio_Sum_var_WM_Sum_var_GM",	"Asymmetry_Index_Skew_WM_Skew_GM",	"Symmetry_Index_Skew_WM_Skew_GM",	"Difference_Skew_WM_Skew_GM",	"Ratio_Skew_WM_Skew_GM",	"Asymmetry_Index_Sum_Aver_WM_Sum_Aver_GM",	"Symmetry_Index_Sum_Aver_WM_Sum_Aver_GM",	"Difference_Sum_Aver_WM_Sum_Aver_GM",	"Ratio_Sum_Aver_WM_Sum_Aver_GM",	"Asymmetry_Index_contrast_WM_contrast_GM",	"Symmetry_Index_contrast_WM_contrast_GM",	"Difference_contrast_WM_contrast_GM",	"Ratio_contrast_WM_contrast_GM")
  
  # Initialize an empty data frame to store results
  results_df <- data.frame("Statistic" = c("Mean_Positive", "SD_Positive", "Mean_Negative", "SD_Negative", "T-value", "P-value"))
  
  # Loop over each outcome column
  for (outcome_col in outcome_columns) {
    # Calculate mean and standard deviation for positive and negative groups
    mean_positive <- mean(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    sd_positive <- sd(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    mean_negative <- mean(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    sd_negative <- sd(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    
    # Perform GLM with AGE as a covariate for the current outcome column
    glm_model <- glm(df[[outcome_col]] ~ df$Amyloid_s_th + age, family = gaussian(link = "identity"))
    
    # Extract t-value and p-value for the Amyloid_s_th effect
    summary_glm <- summary(glm_model)
    t_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "t value"]
    p_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "Pr(>|t|)"]
    
    # Add the results to the data frame
    results_df[outcome_col] <- c(mean_positive, sd_positive, mean_negative, sd_negative, t_value, p_value)
  }
  
  # Return the results data frame
  return(results_df)
}

# Initialize a list to store results for all x values
all_results <- list()

# Loop over each x value and perform the analysis
for (x in x_values) {
  results <- perform_glm_analysis(x)
  all_results[[paste0("x_", x)]] <- results
}

# Print the results for each x value
for (x in names(all_results)) {
  cat("Results for x =", x, ":\n")
  print(all_results[[x]])
  cat("\n")
}





# Define the x values
x_values <- c(
  31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 
  114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 
  133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 
  148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 
  165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 
  181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 
  200, 201, 202, 203, 204, 205, 206, 207
)

# Define a function to perform the GLM analysis for a given x value
perform_glm_analysis <- function(x) {
  # Construct the file path based on the current x value
  file_path <- paste0("/Users/demoranky/documents/water/final_", x, "_GM_WM.csv")
  
  # Check if the file exists
  if (!file.exists(file_path)) {
    stop("File not found: ", file_path)
  }
  
  # Read the CSV file
  df <- read.csv(file_path)
  
  # Specify the covariate column
  age <- df$AGE
  
  # Define a list of outcome columns to analyze
  outcome_columns <- c(
    "Symmetry_Index_IDM_WM_IDM_GM", "Difference_IDM_WM_IDM_GM", "Ratio_IDM_WM_IDM_GM", 
    "Asymmetry_Index_TotalEnergy_WM_TotalEnergy_GM", "Symmetry_Index_TotalEnergy_WM_TotalEnergy_GM", 
    "Difference_TotalEnergy_WM_TotalEnergy_GM", "Ratio_TotalEnergy_WM_TotalEnergy_GM", 
    "Asymmetry_Index_entropy_WM_entropy_GM", "Symmetry_Index_entropy_WM_entropy_GM", 
    "Difference_entropy_WM_entropy_GM", "Ratio_entropy_WM_entropy_GM", 
    "Asymmetry_Index_kurtosis_WM_kurtosis_GM", "Symmetry_Index_kurtosis_WM_kurtosis_GM", 
    "Difference_kurtosis_WM_kurtosis_GM", "Ratio_kurtosis_WM_kurtosis_GM", 
    "Asymmetry_Index_Sum_var_WM_Sum_var_GM", "Symmetry_Index_Sum_var_WM_Sum_var_GM", 
    "Difference_Sum_var_WM_Sum_var_GM", "Ratio_Sum_var_WM_Sum_var_GM", 
    "Asymmetry_Index_Skew_WM_Skew_GM", "Symmetry_Index_Skew_WM_Skew_GM", 
    "Difference_Skew_WM_Skew_GM", "Ratio_Skew_WM_Skew_GM", 
    "Asymmetry_Index_Sum_Aver_WM_Sum_Aver_GM", "Symmetry_Index_Sum_Aver_WM_Sum_Aver_GM", 
    "Difference_Sum_Aver_WM_Sum_Aver_GM", "Ratio_Sum_Aver_WM_Sum_Aver_GM", 
    "Asymmetry_Index_contrast_WM_contrast_GM", "Symmetry_Index_contrast_WM_contrast_GM", 
    "Difference_contrast_WM_contrast_GM", "Ratio_contrast_WM_contrast_GM"
  )
  
  # Initialize an empty data frame to store results
  results_df <- data.frame("Statistic" = c("Mean_Positive", "SD_Positive", "Mean_Negative", "SD_Negative", "T-value", "P-value"))
  
  # Loop over each outcome column
  for (outcome_col in outcome_columns) {
    # Calculate mean and standard deviation for positive and negative groups
    mean_positive <- mean(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    sd_positive <- sd(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    mean_negative <- mean(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    sd_negative <- sd(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    
    # Perform GLM with AGE as a covariate for the current outcome column
    glm_model <- glm(df[[outcome_col]] ~ df$Amyloid_s_th + age, family = gaussian(link = "identity"))
    
    # Extract t-value and p-value for the Amyloid_s_th effect
    summary_glm <- summary(glm_model)
    t_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "t value"]
    p_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "Pr(>|t|)"]
    
    # Add the results to the data frame
    results_df[outcome_col] <- c(mean_positive, sd_positive, mean_negative, sd_negative, t_value, p_value)
  }
  
  # Save the results to a CSV file
  output_file_path <- paste0("/Users/demoranky/documents/water1/results_", x, "_GM_WM_agg_LM.csv")
  write.csv(results_df, file = output_file_path, row.names = FALSE)
  
  return(output_file_path)
}

# Loop over each x value and perform the analysis
for (x in x_values) {
  tryCatch({
    output_file_path <- perform_glm_analysis(x)
    cat("Results saved to:", output_file_path, "\n")
  }, error = function(e) {
    cat("An error occurred for x =", x, ": ", e$message, "\n")
  })
}






# Define the x values
x_values <- c(
  31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 
  114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 
  133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 
  148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 
  165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 
  181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 
  200, 201, 202, 203, 204, 205, 206, 207
)

# Define a function to perform the GLM analysis for a given x value
perform_glm_analysis <- function(x) {
  # Construct the file path based on the current x value
  file_path <- paste0("/Users/demoranky/documents/water/final_", x, "_GM_WM.csv")
  
  # Check if the file exists
  if (!file.exists(file_path)) {
    stop("File not found: ", file_path)
  }
  
  # Read the CSV file
  df <- read.csv(file_path)
  
  # Specify the covariate column
  age <- df$AGE
  
  # Define a list of outcome columns to analyze
  outcome_columns <- c(
    "Symmetry_Index_IDM_WM_IDM_GM", "Difference_IDM_WM_IDM_GM", "Ratio_IDM_WM_IDM_GM", 
    "Asymmetry_Index_TotalEnergy_WM_TotalEnergy_GM", "Symmetry_Index_TotalEnergy_WM_TotalEnergy_GM", 
    "Difference_TotalEnergy_WM_TotalEnergy_GM", "Ratio_TotalEnergy_WM_TotalEnergy_GM", 
    "Asymmetry_Index_entropy_WM_entropy_GM", "Symmetry_Index_entropy_WM_entropy_GM", 
    "Difference_entropy_WM_entropy_GM", "Ratio_entropy_WM_entropy_GM", 
    "Asymmetry_Index_kurtosis_WM_kurtosis_GM", "Symmetry_Index_kurtosis_WM_kurtosis_GM", 
    "Difference_kurtosis_WM_kurtosis_GM", "Ratio_kurtosis_WM_kurtosis_GM", 
    "Asymmetry_Index_Sum_var_WM_Sum_var_GM", "Symmetry_Index_Sum_var_WM_Sum_var_GM", 
    "Difference_Sum_var_WM_Sum_var_GM", "Ratio_Sum_var_WM_Sum_var_GM", 
    "Asymmetry_Index_Skew_WM_Skew_GM", "Symmetry_Index_Skew_WM_Skew_GM", 
    "Difference_Skew_WM_Skew_GM", "Ratio_Skew_WM_Skew_GM", 
    "Asymmetry_Index_Sum_Aver_WM_Sum_Aver_GM", "Symmetry_Index_Sum_Aver_WM_Sum_Aver_GM", 
    "Difference_Sum_Aver_WM_Sum_Aver_GM", "Ratio_Sum_Aver_WM_Sum_Aver_GM", 
    "Asymmetry_Index_contrast_WM_contrast_GM", "Symmetry_Index_contrast_WM_contrast_GM", 
    "Difference_contrast_WM_contrast_GM", "Ratio_contrast_WM_contrast_GM"
  )
  
  # Initialize an empty data frame to store results
  results_df <- data.frame("Statistic" = c("Mean_Positive", "SD_Positive", "Mean_Negative", "SD_Negative", "T-value", "P-value"))
  
  # Loop over each outcome column
  for (outcome_col in outcome_columns) {
    # Calculate mean and standard deviation for positive and negative groups
    mean_positive <- mean(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    sd_positive <- sd(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    mean_negative <- mean(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    sd_negative <- sd(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    
    # Perform GLM with AGE as a covariate for the current outcome column
    glm_model <- glm(df[[outcome_col]] ~ df$Amyloid_s_th + age, family = gaussian(link = "identity"))
    
    # Extract t-value and p-value for the Amyloid_s_th effect
    summary_glm <- summary(glm_model)
    t_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "t value"]
    p_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "Pr(>|t|)"]
    
    # Add the results to the data frame
    results_df[outcome_col] <- c(mean_positive, sd_positive, mean_negative, sd_negative, t_value, p_value)
  }
  
  # Add the x value as a column
  results_df$x <- x
  
  # Return the results data frame
  return(results_df)
}

# Initialize an empty list to store results for all x values
all_results <- list()

# Loop over each x value and perform the analysis
for (x in x_values) {
  tryCatch({
    results <- perform_glm_analysis(x)
    all_results[[paste0("x_", x)]] <- results
  }, error = function(e) {
    cat("An error occurred for x =", x, ": ", e$message, "\n")
  })
}

# Combine all results into a single data frame
combined_results <- do.call(rbind, all_results)

# Save the combined results to a CSV file
output_file_path <- "/Users/demoranky/documents/water1/combined_results_LM.csv"
write.csv(combined_results, file = output_file_path, row.names = FALSE)

cat("All results combined and saved to:", output_file_path, "\n")








# Define the x values
x_values <- c(
  31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 
  114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 
  133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 
  148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 
  165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 
  181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 
  200, 201, 202, 203, 204, 205, 206, 207
)

# Define a function to perform the GLM analysis for a given x value
perform_glm_analysis <- function(x) {
  # Construct the file path based on the current x value
  file_path <- paste0("/Users/demoranky/documents/water/final_", x, "_GM_WM.csv")
  
  # Check if the file exists
  if (!file.exists(file_path)) {
    stop("File not found: ", file_path)
  }
  
  # Read the CSV file
  df <- read.csv(file_path)
  
  # Specify the covariate column
  age <- df$AGE
  
  # Define a list of outcome columns to analyze
  outcome_columns <- c(
    "Symmetry_Index_IDM_WM_IDM_GM", "Difference_IDM_WM_IDM_GM", "Ratio_IDM_WM_IDM_GM", 
    "Asymmetry_Index_TotalEnergy_WM_TotalEnergy_GM", "Symmetry_Index_TotalEnergy_WM_TotalEnergy_GM", 
    "Difference_TotalEnergy_WM_TotalEnergy_GM", "Ratio_TotalEnergy_WM_TotalEnergy_GM", 
    "Asymmetry_Index_entropy_WM_entropy_GM", "Symmetry_Index_entropy_WM_entropy_GM", 
    "Difference_entropy_WM_entropy_GM", "Ratio_entropy_WM_entropy_GM", 
    "Asymmetry_Index_kurtosis_WM_kurtosis_GM", "Symmetry_Index_kurtosis_WM_kurtosis_GM", 
    "Difference_kurtosis_WM_kurtosis_GM", "Ratio_kurtosis_WM_kurtosis_GM", 
    "Asymmetry_Index_Sum_var_WM_Sum_var_GM", "Symmetry_Index_Sum_var_WM_Sum_var_GM", 
    "Difference_Sum_var_WM_Sum_var_GM", "Ratio_Sum_var_WM_Sum_var_GM", 
    "Asymmetry_Index_Skew_WM_Skew_GM", "Symmetry_Index_Skew_WM_Skew_GM", 
    "Difference_Skew_WM_Skew_GM", "Ratio_Skew_WM_Skew_GM", 
    "Asymmetry_Index_Sum_Aver_WM_Sum_Aver_GM", "Symmetry_Index_Sum_Aver_WM_Sum_Aver_GM", 
    "Difference_Sum_Aver_WM_Sum_Aver_GM", "Ratio_Sum_Aver_WM_Sum_Aver_GM", 
    "Asymmetry_Index_contrast_WM_contrast_GM", "Symmetry_Index_contrast_WM_contrast_GM", 
    "Difference_contrast_WM_contrast_GM", "Ratio_contrast_WM_contrast_GM"
  )
  
  # Initialize an empty data frame to store results
  results_df <- data.frame("Statistic" = c("Mean_Positive", "SD_Positive", "Mean_Negative", "SD_Negative", "T-value", "P-value"))
  
  # Loop over each outcome column
  for (outcome_col in outcome_columns) {
    # Calculate mean and standard deviation for positive and negative groups
    mean_positive <- mean(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    sd_positive <- sd(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    mean_negative <- mean(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    sd_negative <- sd(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    
    # Perform GLM with AGE as a covariate for the current outcome column
    glm_model <- glm(df[[outcome_col]] ~ df$Amyloid_s_th + age, family = gaussian(link = "identity"))
    
    # Extract t-value and p-value for the Amyloid_s_th effect
    summary_glm <- summary(glm_model)
    t_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "t value"]
    p_value <- summary_glm$coefficients["df$Amyloid_s_thPositive", "Pr(>|t|)"]
    
    # Add spaces to the results
    mean_positive <- paste0(" ", mean_positive)
    sd_positive <- paste0(" ", sd_positive)
    mean_negative <- paste0(" ", mean_negative)
    sd_negative <- paste0(" ", sd_negative)
    t_value <- paste0(" ", t_value)
    p_value <- paste0(" ", p_value)
    
    # Add the results to the data frame
    results_df[outcome_col] <- c(mean_positive, sd_positive, mean_negative, sd_negative, t_value, p_value)
  }
  
  # Add the x value as a column
  results_df$x <- x
  
  # Return the results data frame
  return(results_df)
}

# Initialize an empty list to store results for all x values
all_results <- list()

# Loop over each x value and perform the analysis
for (x in x_values) {
  tryCatch({
    results <- perform_glm_analysis(x)
    all_results[[paste0("x_", x)]] <- results
  }, error = function(e) {
    cat("An error occurred for x =", x, ": ", e$message, "\n")
  })
}

# Combine all results into a single data frame
combined_results <- do.call(rbind, all_results)

# Save the combined results to a CSV file
output_file_path <- "/Users/demoranky/documents/water1/combined_results_LM.csv"
write.csv(combined_results, file = output_file_path, row.names = FALSE)

cat("All results combined and saved to:", output_file_path, "\n")













library(dplyr)

# Define the x values
x_values <- c(
  31, 32, 47, 48, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 112, 113, 
  114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 128, 129, 132, 
  133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 
  148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 160, 161, 162, 163, 164, 
  165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 
  181, 182, 183, 184, 185, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 
  200, 201, 202, 203, 204, 205, 206, 207
)

# Define a function to perform the GLM analysis for a given x value
perform_glm_analysis <- function(x) {
  # Construct the file path based on the current x value
  file_path <- paste0("/Users/demoranky/documents/water/final_ATF_", x, ".csv")
  
  # Check if the file exists
  if (!file.exists(file_path)) {
    stop("File not found: ", file_path)
  }
  
  # Read the CSV file
  df <- read.csv(file_path)
  
  # Specify the covariate column
  age <- df$AGE
  
  # Define a list of outcome columns to analyze
  outcome_columns <- c("ALF_IDM", "ATF_IDM1", "ALF_TE", "ATF_TE1", "ALF_EN", "ATF_EN1", 
                       "ALF_KU", "ATF_KU1", "ALF_SV", "ATF_SV1", "ALF_SK", "ATF_SK1")
  
  # Initialize an empty data frame to store results
  results_df <- data.frame("Statistic" = c("Mean_Positive", "SD_Positive", "Mean_Negative", "SD_Negative", "T-value", "P-value"))
  
  # Loop over each outcome column
  for (outcome_col in outcome_columns) {
    # Calculate mean and standard deviation for positive and negative groups
    mean_positive <- mean(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    sd_positive <- sd(df[df$Amyloid_s_th == "Positive", outcome_col], na.rm = TRUE)
    mean_negative <- mean(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    sd_negative <- sd(df[df$Amyloid_s_th == "Negative", outcome_col], na.rm = TRUE)
    
    # Perform GLM with AGE as a covariate for the current outcome column
    glm_model <- glm(as.formula(paste(outcome_col, "~ Amyloid_s_th + age")), data = df, family = gaussian(link = "identity"))
    
    # Extract t-value and p-value for the Amyloid_s_th effect
    summary_glm <- summary(glm_model)
    t_value <- summary_glm$coefficients["Amyloid_s_thPositive", "t value"]
    p_value <- summary_glm$coefficients["Amyloid_s_thPositive", "Pr(>|t|)"]
    
    # Add the results to the data frame
    results_df[outcome_col] <- c(mean_positive, sd_positive, mean_negative, sd_negative, t_value, p_value)
  }
  
  # Add the x value as a column
  results_df$x <- x
  
  # Return the results data frame
  return(results_df)
}

# Initialize an empty list to store results for all x values
all_results <- list()

# Loop over each x value and perform the analysis
for (x in x_values) {
  tryCatch({
    results <- perform_glm_analysis(x)
    all_results[[paste0("x_", x)]] <- results
  }, error = function(e) {
    cat("An error occurred for x =", x, ": ", e$message, "\n")
  })
}

# Combine all results into a single data frame
combined_results <- do.call(rbind, all_results)

# Save the combined results to a CSV file
output_file_path <- "/Users/demoranky/documents/water1/combined_ATF_results_LM.csv"
write.csv(combined_results, file = output_file_path, row.names = FALSE)

cat("All results combined and saved to:", output_file_path, "\n")
