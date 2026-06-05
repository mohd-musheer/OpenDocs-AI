
# Drop Constant Columns - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/drop_constant_columns.html

Algorithm
Drop Constant Columns
Description
Removes columns that have zero variance.
Implementation Details
Implemented in C++ (`LinearRegression.cpp`).
// Check variance
if(var < eps) {
dropped_cols.push_back(j);
} else {
keep_cols.push_back(j);
// Copy column
}
Use Cases
General purpose.
