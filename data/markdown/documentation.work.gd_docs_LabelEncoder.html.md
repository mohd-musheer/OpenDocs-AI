
# Label Encoder - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/LabelEncoder.html

Algorithm
Label Encoder
Description
Encodes target labels with value between 0 and n_classes-1.
Implementation Details
Implemented in `encoders.R`.
fit=function(x){
vals <- unique(x)
map <<- setNames(seq_along(vals)-1, vals)
},
transform=function(x){
as.numeric(map[x])
}
Use Cases
General purpose.
