
# One Hot Encoder - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/OneHotEncoder.html

Algorithm
One Hot Encoder
Description
Encodes categorical features as a one-hot numeric array.
Implementation Details
Implemented in `encoders.R`.
transform=function(df){
# ... setup code ...
for(colname in names(df)){
col <- as.character(df[[colname]])
cats <- categories[[colname]]
idx <- match(col, cats)
# ... fill matrix ...
out[cbind(row_ids, col_ids)] <- 1L
}
out
}
Use Cases
General purpose.
