df=read.delim("/Users/cmdb/qbb2016-answers/week11/hema_data.txt", header = T)
d <- dist(df, method = "euclidean")
fit <- hclust(d, method = "complete")
##plot(fit)
rownames(df) <- df$gene
df_matrix <- as.matrix(df[2:7])
head(df_matrix)
heatmap(df_matrix)


df=read.delim("/Users/cmdb/qbb2016-answers/week11/hema_data.txt", header = T)
d <- dist(df, method = "euclidean")
fit <- hclust(d, method = "complete")
##svg(width = 50)
##plot(fit, hang=-1, cex=0.5)
##svg(width=50)
##plot(fit, hang=-1, cex=0.5)
##dev.off()

rownames(df) <- df$gene
df_matrix <- as.matrix(df[2:7])
head(df_matrix)
hm <- heatmap(df_matrix, keep.dendro = TRUE)
hc <- as.hclust( hm$rowDendrogram )

##table(df_matrix)
heatmap(df_matrix)
hc <- as.hclust( hm$rowDendrogram )
cutree( hc, h=10 )


library("ggplot2")

set.seed(20)
dfcluster <- kmeans(df[, 2:3], 5, nstart = 20)
dfcluster$cluster <- as.factor(dfcluster$cluster)
ggplot(df, aes(CFU, poly, color = dfcluster$cluster) ) + geom_point()

set.seed(20)
dfcluster <- kmeans(df[, 2:3], 3, nstart = 20)
dfcluster$cluster <- as.factor(dfcluster$cluster)
ggplot(df, aes(CFU, poly, color = dfcluster$cluster) ) + geom_point()

t.test(df$CFU, df$poly, paired = TRUE)

df$early <- ave(df$CFU, df$mys)
df$late <- ave(df$poly, df$unk)
t.test(df$early, df$late, paired = TRUE)
df$diff <- (df$late - df$early)

df <- df[,-c(ncol(df))]
df$diff <- NULL

df$ratio <- (df$late/df$early)
diff_genes <- df[df$ratio > 2 | df$ratio < 0.5, ]
diff_genes_all_data <- df[df$ratio > 2 | df$ratio < 0.5, ]
differentially_expressed_genes <- diff_genes$gene
diff_genes$CFU  <- NULL 
diff_genes$poly <- NULL 
diff_genes$unk <- NULL 
diff_genes$int <- NULL 
diff_genes$mys <- NULL 
diff_genes$mid <- NULL 
diff_genes$early <- NULL
diff_genes$late <- NULL

t.test(diff_genes_all_data$early, diff_genes_all_data$late, paired = TRUE)

write.table(diff_genes, "/Users/cmdb/qbb2016-answers/week11/diff_genes.txt", sep="\t")


gene_list <- diff_genes
gene_list$ratio <- NULL
gene_list$gene <- NULL

write.table(gene_list, "/Users/cmdb/qbb2016-answers/week11/gene_list.txt")
library(xlsx)
write.xlsx(gene_list, "/Users/cmdb/qbb2016-answers/week11/gene_list.xlsx")






