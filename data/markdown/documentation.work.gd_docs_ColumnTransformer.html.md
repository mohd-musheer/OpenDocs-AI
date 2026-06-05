
# Column Transformer - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/ColumnTransformer.html

Algorithm
Column Transformer
Description
Applies transformers to columns of an array or pandas DataFrame.
Implementation Details
Implemented in `column_transformer.R`.
transform=function(df){
# ...
if(!is.null(num_pipeline) && length(num_cols) > 0L){
parts[[length(parts)+1]] <-
as_feature_matrix(num_pipeline$transform(df[,num_cols,drop=FALSE]))
}
# ... same for cat_pipeline ...
out <- do.call(cbind, parts)
out
}
Use Cases
General purpose.
