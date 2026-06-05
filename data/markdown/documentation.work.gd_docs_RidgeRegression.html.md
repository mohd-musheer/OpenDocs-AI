
# Ridge Regression - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/RidgeRegression.html

Algorithm
Ridge Regression
Description
A regularized linear regression method that solves the ill-posed problem where features are highly correlated (multicollinearity). By adding an L2 penalty to the loss function, it shrinks the coefficients towards zero, reducing model variance. Our implementation efficiently adds this penalty directly to the Gram matrix ($X^T X$) before solving, utilizing the same optimized BLAS routines as standard Linear Regression.
$$ \hat{\beta}^{ridge} = (X^T X + \lambda I)^{-1} X^T y $$
Algorithm Workflow
START
Receive Matrix X and Vector y.
COMPUTE
Calculate the covariance/Gram matrix $A = X^T X$.
REGULARIZE
Add $\lambda$ (alpha) to the diagonal elements: $A_{ii} \leftarrow
A_{ii} + \lambda$.
RHS
Calculate the right-hand side vector $b = X^T y$.
SOLVE
Solve the linear system $A \beta = b$ using Cholesky
Decomposition.
FALLBACK
If Cholesky fails (rare), use LU Decomposition.
END
Return robust coefficients $\beta$.
Implementation Details
Implemented in `RidgeRegression.cpp`.
// Add regularization
for(int j=0; j<p; ++j)
XtX[j + j*p] += alpha;
// Solve
F77_CALL(dposv)(...);
Complexity & Optimization
Time Complexity
O(N * P^2).
Space Complexity
O(P^2).
Optimizations
Cholesky Solver.
Limitations
No feature selection.
Use Cases
Correlated features.
