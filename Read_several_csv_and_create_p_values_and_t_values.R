# Install and load required packages
install.packages("boom")
install.packages("dplyr")

# Load required libraries
library(boom)
library(dplyr)

# Replace '...' with the path to the directory with your files.
files <- list.files('/Users/demoranky/documents/New_all_ADNI_groups/', pattern="\\used.csv$", full.names=TRUE)
files <- setNames(files, basename(files))

# Function to perform GLM and extract p-values
results <- lapply(files,  function(x) {
  
  # Read data from CSV file
  df <- read.csv(x, stringsAsFactors=FALSE)
  
  # Fit GLMs
  result <- glm(TotalEnergy_WM ~ Amyloid_s_th + AGE, data = df)
  result1 <- glm(TotalEnergy_GM ~ Amyloid_s_th + AGE, data = df)
  result2 <- glm(IDM_GM ~ Amyloid_s_th + AGE, data = df)
  result3 <- glm(IDM_WM ~ Amyloid_s_th + AGE, data = df)
  
  # Extract p-values
  TotalEnergy_WM <- summary(result)$coefficients[,"Pr(>|t|)"][[2]]
  TotalEnergy_GM <- summary(result1)$coefficients[,"Pr(>|t|)"][[2]]
  IDM_GM <- summary(result2)$coefficients[,"Pr(>|t|)"][[2]]
  IDM_WM <- summary(result3)$coefficients[,"Pr(>|t|)"][[2]]
  
  # Combine p-values into a data frame
  R1 <- data.frame(TotalEnergy_GM, TotalEnergy_WM, IDM_GM, IDM_WM)
  
  # Create table and assign chart data attributes
  H <- cbind(TotalEnergy_GM, TotalEnergy_WM, IDM_GM, IDM_WM)
  R2 <- as.table(H)
  attr(R2, "ChartData")
  
  return(R2)
})-> resultpp

resultpp

# Function to perform GLM and extract t-values
resultkk <- lapply(files,  function(x) {
  
  # Read data from CSV file
  df1 <- read.csv(x, stringsAsFactors=FALSE)
  
  # Fit GLMs
  resulta <- glm(TotalEnergy_WM ~ Amyloid_s_th + AGE, data = df1)
  resultb <- glm(TotalEnergy_GM ~ Amyloid_s_th + AGE, data = df1)
  resultc <- glm(IDM_GM ~ Amyloid_s_th + AGE, data = df1)
  resultd <- glm(IDM_WM ~ Amyloid_s_th + AGE, data = df1)
  
  # Extract t-values
  TotalEnergy_WM <- summary(resulta)$coefficients[, "t value"][[2]]
  TotalEnergy_GM <- summary(resultb)$coefficients[, "t value"][[2]]
  IDM_GM <- summary(resultc)$coefficients[, "t value"][[2]]
  IDM_WM <- summary(resultd)$coefficients[, "t value"][[2]]
  
  # Combine t-values into a data frame
  Rk <- data.frame(TotalEnergy_GM, TotalEnergy_WM, IDM_GM, IDM_WM)
  
  # Create table and assign chart data attributes
  Hk <- cbind(TotalEnergy_GM, TotalEnergy_WM, IDM_GM, IDM_WM)
  Rk2 <- as.table(Hk)
  attr(Rk2, "ChartData")
  
  return(Rk2)
})-> resultpp2

resultpp2

# Combine results from both p-values and t-values
H <- cbind(resultpp, resultpp2)
Ror <- as.table(H)

# Write results to a CSV file
write.csv(Ror, file = '/Users/demoranky/documents/check2.csv')
