rm(list=ls())

library(aplpack)
library(dplyr)

beerstats <- tbl_df(read.csv('beerstats.csv', header=TRUE))
beerstats <- beerstats %>% mutate(
    og=(og_low + og_high)/2,
    fg=(fg_low + fg_high)/2,
    ibu=(ibu_low + ibu_high)/2,
    srm=(srm_low + srm_high)/2,
    abv=(abv_low + abv_high)/2)

png(file="beerfaces.png", width=960, height=1920)
faces(beerstats[c("og", "fg", "ibu", "srm", "abv")],
      labels=beerstats$name,
      nrow.plot=15,
      ncol.plot=5)
dev.off()
