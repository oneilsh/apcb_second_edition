#!/usr/bin/env Rscript

library(stringr)
library(dplyr)

## This script analyzes the data stored in the data frame
## expr_long_split.Rdata, containing gene expression data

load("expr_long_split.Rdata")
expr <- expr_long_split

## Given a data frame with columns for expression,
## genotype, and treatement, runs a linear model
## and returns a single-row data frame with p-values in columns
sub_df_to_pvals_df <- function(sub_df) {
  lm1 <- lm(expression ~ genotype + treatment + genotype:treatment,
            data = sub_df)

  anova1 <- anova(lm1)
  pvals1 <- anova1$"Pr(>F)"
  pvals_list1 <- as.list(pvals1)
  pvals_df1 <- data.frame(pvals_list1)
  colnames(pvals_df1) <- rownames(anova1)

  return(pvals_df1)
}

uniq_ids <- unique(expr$id)
expr1 <- expr[expr$id %in% uniq_ids[1], ]

pvals_df1 <- sub_df_to_pvals_df(expr1)

## Run all data
expr_by_id <- group_by(expr, id)
pvals_df <- do(expr_by_id, sub_df_to_pvals_df(.))

## Add BY-adjusted column
pvals_df$interaction_BY <- p.adjust(pvals_df$"genotype:treatment")

## Extract with BY-adjusted FDR < 0.05
pvals_interaction_sig <- pvals_df[pvals_df$interaction_BY < 0.05, ]
print(pvals_interaction_sig)