# Replace '...' with the path to the directory with your files.
files <- list.files('/Users/demoranky/downloads/Data_to_dave_sandy/', pattern="\\IDM_TE.csv$", full.names=TRUE)
files <- setNames(files, basename(files))

results <- lapply(files,  function(x) {
  dj <- read.csv(x, stringsAsFactors=FALSE)
  Rp<- data.frame(dj)
  #Rj <-as.table(Rp)
  return(Rp)
})-> rje

rje
write.csv(rje, file='/Users/demoranky/documents/ABC_group_combine.csv')