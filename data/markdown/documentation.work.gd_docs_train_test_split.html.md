
# Train Test Split - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/train_test_split.html

Algorithm
Train Test Split
Description
Split arrays or matrices into random train and test subsets.
Implementation Details
Implemented in `split.R`.
train_test_split <- function(X,y,test_size=0.2, seed=NULL){
if(!is.null(seed)) set.seed(seed)
n <- nrow(X)
idx <- sample(n)
split <- max(2, floor(n*(1-test_size)))
train_idx <- idx[1:split]
test_idx <- idx[(split+1):n]
list(X_train=X[train_idx,,drop=FALSE], X_test=X[test_idx,,drop=FALSE],
y_train=y[train_idx], y_test=y[test_idx])
}
Use Cases
General purpose.
