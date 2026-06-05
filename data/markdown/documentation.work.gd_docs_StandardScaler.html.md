
# Standard Scaler - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/StandardScaler.html

Algorithm
Standard Scaler
Description
Standardizes features by removing the mean and scaling to unit variance.
Implementation Details
Implemented in `scalers.R`. Uses `cpp_scale_fit_transform` for speed if available, otherwise R `scale`.
fit=function(X){
X <- as.matrix(X)
if (exists("cpp_scale_fit_transform", mode="function")) {
out <- cpp_scale_fit_transform(X)
mean <<- out$mean
sd <<- out$sd
} else {
mean <<- colMeans(X)
sd <<- apply(X,2,sd)
sd[sd==0] <<- 1
}
}
Complexity & Optimization
Time Complexity
O(N * P).
Space Complexity
O(P).
Optimizations
None
Limitations
None listed
Use Cases
General purpose.
