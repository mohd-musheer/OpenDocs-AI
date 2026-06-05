
# Linear Regression - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/LinearRegression.html

Algorithm
Linear Regression
Description
A fundamental statistical method that models the relationship between a scalar response and one or more explanatory variables using a linear predictor functions. This implementation solves the Ordinary Least Squares (OLS) problem using the Normal Equation approach. It is heavily optimized using BLAS (Basic Linear Algebra Subprograms) and LAPACK (Linear Algebra PACKage) for native hardware acceleration, making it suitable for high-performance computing tasks.
$$ \hat{\beta} = (X^T X)^{-1} X^T y $$
Algorithm Workflow
STARTINPUT
Matrix $X$ (Features) and Vector $y$ (Targets).
VALIDATE
Check for row/column consistency and dimensions.
PARALLEL MEAN
Compute $\bar{x}$ for each column via OpenMP SIMD reduction.
GRAM MATRIX
Calculate $X^TX$ using vectorized BLAS `dgemm` (Matrix-Matrix
Mutliplication).
TARGET PROJECTION
Calculate $X^Ty$ using BLAS `dgemv` (Matrix-Vector
Multiplication).
CENTERING
Adjust $X^TX$ and $X^Ty$ using $\bar{x}$ to effectively center the
data.
STABILIZE
Add a small $10^{-8}$ Ridge penalty to the diagonal for numerical
stability.
SOLVE
Apply LAPACK `dposv` (Cholesky Decomposition) to solve $A\beta =
b$.
RECOVERY
If Cholesky fails (singular matrix), trigger Custom Fallback Solver
(LU/QR).
INTERCEPT
Compute $\beta_0 = \bar{y} - \sum (\beta_j \cdot \bar{x}_j)$ derived
from means.
OUTPUT
Store coefficients $\beta$ and intercept $\beta_0$.
PREDICT
Compute standard dot product $X_{new} \cdot \beta + \beta_0$.
Implementation Details
Implemented in `LinearRegression.cpp` using BLAS/LAPACK.
// Compute XtX and Xty using BLAS dgemm/dgemv
F77_CALL(dgemm)("T", "N", &p, &p, &n, &one, x, &n, x, ...);
// Solve using Cholesky (dposv)
F77_CALL(dposv)("L", &n, &one, XtX, &lda, Xty, ...);
Complexity & Optimization
Time Complexity
O(N * P^2).
Space Complexity
O(P^2).
Optimizations
BLAS Level 3.
Limitations
Assumes linearity.
Use Cases
Baseline regression.
