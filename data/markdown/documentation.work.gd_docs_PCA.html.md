
# Principal Component Analysis - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/PCA.html

Algorithm
Principal Component Analysis
Description
A statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components. Our implementation focuses on numerical accuracy using the Covariance method and LAPACK's symmetric eigenvalue solver.
$$ C = \frac{1}{n-1}X^T X, \quad C = V \Lambda V^T $$
Algorithm Workflow
START
Input data matrix $X$.
CENTER
Subtract the mean of each column from the data.
COVARIANCE
Compute the covariance matrix $C = \frac{1}{N-1} X^T X$.
EIGEN
Solving the eigenvalue problem $C v = \lambda v$ using LAPACK
`dsyev`.
SORT
Order eigenvalues $\lambda$ descending and reorder eigenvectors
$v$.
SELECT
Choose the top $k$ eigenvectors corresponding to the largest
eigenvalues.
TRANSFORM
Project $X$ onto the new subspace: $X_{new} = X \cdot V_k$.
END
Return the transformed data and components.
Implementation Details
Implemented in `PCA.cpp` using LAPACK `dsyev` (Symmetric Eigen Value solver). This is numerically robust. The Covariance matrix computation is manual C++ loops.
// Compute Covariance
// ...
// Eigen decomposition
F77_CALL(dsyev)("V", "U", &p, cov.data(), ...);
// Select top k vectors
Complexity & Optimization
Time Complexity
O(P^3).
Space Complexity
O(P^2).
Optimizations
LAPACK dsyev.
Limitations
Linear.
Use Cases
Dimensionality reduction.
