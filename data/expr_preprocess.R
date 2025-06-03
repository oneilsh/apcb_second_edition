#!/usr/bin/env Rscript

library(stringr)

expr_long <- read.table("expr_long_coded.txt",
                        header = TRUE,
                        sep = "\t",
                        stringsAsFactors = FALSE)


# Split sample column into 3-column matrix on _'s
sample_split <- str_split_fixed(expr_long$sample, "_", 3)

# Turn the matrix into a data frame with appropriate column names
# and combine it with the original dataframe into a larger set
sample_split_df <- data.frame(sample_split)
colnames(sample_split_df) <- c("genotype", "treatment", "tissuerep")
expr_long_split <- cbind(expr_long, sample_split_df)

# Create an individual tissue column
expr_long_split$tissue <- NA
expr_long_split$tissue[str_detect(expr_long_split$tissuerep, "A")] <- "A"
expr_long_split$tissue[str_detect(expr_long_split$tissuerep, "B")] <- "B"
expr_long_split$tissue[str_detect(expr_long_split$tissuerep, "C")] <- "C"

# We've already checked for NAs
#print(expr_long_split[is.na(expr_long_split$tissue), ]) # should print 0 rows

# Create a new rep column
expr_long_split$rep <- NA
expr_long_split$rep[str_detect(expr_long_split$tissuerep, "1")] <- "1"
expr_long_split$rep[str_detect(expr_long_split$tissuerep, "2")] <- "2"
expr_long_split$rep[str_detect(expr_long_split$tissuerep, "3")] <- "3"

# We've already checked for NAs, but a few were left
#print(expr_long_split[is.na(expr_long_split$rep), ]) # should print 0 rows

# So we remove all rows with such "bad" IDs
bad_ids <- expr_long_split$id[is.na(expr_long_split$rep)]
bad_rows <- expr_long_split$id %in% bad_ids      # logical vector
expr_long_split <- expr_long_split[!bad_rows, ]  # logical selection

save(expr_long_split, file = "expr_long_split.Rdata")