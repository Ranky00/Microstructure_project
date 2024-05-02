library(tidyverse)
library(readxl)
library(gridExtra)
# Read data
genderweight <- read_csv('/Users/demoranky/documents/ADNI_new_extract/final_100_GM_WM_used.csv')
marte <- read_csv('/Users/demoranky/documents/ADNI_new_extract/final_100_GM_WM_used.csv')

# Reshape data for IDM
marte_glc <- gather(marte, "IDM_WM", "IDM_GM", key = "IDM", value = "value")
marte_glc$group <- as.factor(marte_glc$Amyloid_s_th)
marte_glc$gene <- as.factor(marte_glc$IDM)

# Reshape data for TotalEnergy
marte_glszm <- gather(marte, "TotalEnergy_GM", "TotalEnergy_WM", key = "TotalEnergy", value = "value")
marte_glszm$group <- as.factor(marte_glszm$Amyloid_s_th)
marte_glszm$gene <- as.factor(marte_glszm$TotalEnergy)

# Compare means for IDM
my_comparisons <- list(c("CN", "AD"), c("CN", "MCI"), c("MCI", "AD"))
compare_means(IDM_WM ~ Amyloid_s_th, data = genderweight)

# Compare means for TotalEnergy
compare_means(TotalEnergy_WM ~ Amyloid_s_th, data = genderweight)

# Plot for IDM and TotalEnergy side by side
plot_IDM <- ggplot(marte_glc, aes(x = IDM, y = value, color = group)) +
  geom_boxplot() +
  stat_compare_means(comparisons = my_comparisons) +
  stat_compare_means(label.y = 1.2) +
  geom_boxplot(outlier.shape = NA) +
  geom_point(position = position_jitterdodge(), alpha = 0.3) +
  scale_color_manual(values = c("blue", "red")) +
  ggtitle("IDM")

plot_TotalEnergy <- ggplot(marte_glszm, aes(x = TotalEnergy, y = value, color = group)) +
  geom_boxplot() +
  stat_compare_means(comparisons = my_comparisons) +
  stat_compare_means(label.y = 1.2) +
  geom_boxplot(outlier.shape = NA) +
  geom_point(position = position_jitterdodge(), alpha = 0.3) +
  scale_color_manual(values = c("blue", "red")) +
  ggtitle("Total Energy")

# Plot both graphs side by side
grid.arrange(plot_IDM, plot_TotalEnergy, ncol = 2)
