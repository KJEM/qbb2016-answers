df <- read.delim("/Users/cmdb/qbb2016-answers/week_5/plink.eigenvec", header = F, sep= " ")

colnames(df)[3] <- "A01"
plot(df$A01,df$V4,)

df2 <- read.delim("/Users/cmdb/qbb2016-answers/week_5/alleles.txt", header = T, sep = "\t")
hist(df2$MAF, breaks = 100, col = "blue")

file = list.files("~/qbb2016-answers/week_5/", pattern = ".*qassoc", full.names = "T" )


for (i in file){
  df3 <- read.delim(i, header = T )
  name = gsub("/Users/cmdb/qbb2016-answers/week_5//plink.", "", i)
  name = gsub(".qassoc", "", name)
  for (j in 1:nrow(df3)){
    if (df3[j,9] < .00001) {df3[j,10]="blue"}
    else {df3[j,10]="black"}
    
  }
  newname = gsub("qassoc", "png", i)
  par(mar=c(5,5,2,2))
  png(newname, width = 6, height = 3.5, units = "in", res= 1200, pointsize = 5)
  plot(rownames(df3), -log(df3$P), col = adjustcolor(df3$X, alpha.f = .5), pch = 16, cex = .5, xaxt = "n", xlab = "Chromosome Position", ylab = "-log(p value)", main = paste("GWAS", name))
  axis(1, c(1, 209, 1112, 1280, 2546, 3109, 3444, 4538, 4980, 5526, 6383, 7220, 8432, 9273, 9907, 10999), c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"), cex.axis = .75)
  abline(a = -log(.00001), b = 0, lwd = 3, lty = 4, col = "red")
  dev.off() 
}
