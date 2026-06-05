
# Min-Max Scaler - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/MinMaxScaler.html

Algorithm
Min-Max Scaler
Description
Transforms features by scaling each feature to a given range.
Implementation Details
Implemented in `scalers.R`.
transform=function(X){
X <- as.matrix(X)
(X - minv)/(maxv - minv + 1e-8)
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
