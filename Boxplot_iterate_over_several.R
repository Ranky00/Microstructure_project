# Load necessary libraries
library(tidyverse)
library(ggpubr)

# Iterate over x values
for (x in c(32, 47, 48)) {
  # Define file path
  file_path <- paste0("/Users/demoranky/documents/water_LBP/final_", x, "_GM_WM_PCA.csv")
  
  # Read data from CSV file
  data <- read_csv(file_path)
  
  # Ensure only two groups and numeric value columns
  data <- data %>%
    filter(Amyloid_s_th %in% c("Negative", "Positive")) %>%
    mutate(PC1_WM = as.numeric(PC1_WM),
           PC1_GM = as.numeric(PC1_GM))
  
  # Check if value columns are numeric
  if (!is.numeric(data$PC1_WM) | !is.numeric(data$PC1_GM)) {
    stop("Error: 'PC1_WM' and 'PC1_GM' columns must be numeric for boxplot.")
  }
  
  # Calculate p-values using Wilcoxon test for both columns
  p_value_wm <- wilcox.test(PC1_WM ~ Amyloid_s_th, data = data)$p.value
  p_value_gm <- wilcox.test(PC1_GM ~ Amyloid_s_th, data = data)$p.value
  
  # Create the boxplots with ggplot2
  plot_PC1_WM <- ggplot(data, aes(x = Amyloid_s_th, y = PC1_WM, color = Amyloid_s_th)) +
    geom_boxplot(outlier.shape = NA) +
    geom_jitter(alpha = 0.3) +
    stat_summary(fun = median, geom = "point", size = 3, color = "black") +  
    labs(title = paste("PC1 WM -", x), x = "Group", y = "PC1 WM Value") +
    theme_bw() +
    scale_color_manual(values = c("blue", "red")) +
    annotate("text", x = 1.5, y = max(data$PC1_WM, na.rm = TRUE) * 1.1, 
             label = paste("p-value:", format.pval(p_value_wm, digits = 3)), hjust = 0.5)
  
  plot_PC1_GM <- ggplot(data, aes(x = Amyloid_s_th, y = PC1_GM, color = Amyloid_s_th)) +
    geom_boxplot(outlier.shape = NA) +
    geom_jitter(alpha = 0.3) +
    stat_summary(fun = median, geom = "point", size = 3, color = "black") +  
    labs(title = paste("PC1 GM -", x), x = "Group", y = "PC1 GM Value") +
    theme_bw() +
    scale_color_manual(values = c("blue", "red")) +
    annotate("text", x = 1.5, y = max(data$PC1_GM, na.rm = TRUE) * 1.1, 
             label = paste("p-value:", format.pval(p_value_gm, digits = 3)), hjust = 0.5)
  
  # Arrange plots side by side
  grid.arrange(plot_PC1_WM, plot_PC1_GM, ncol = 2)
  
  # Save the plots
  ggsave(paste0("/Users/demoranky/documents/water_LBP/", x, "_boxplot_PC1_WM_GM.png"), 
         arrangeGrob(plot_PC1_WM, plot_PC1_GM, ncol = 2), width = 12, height = 6)
}
