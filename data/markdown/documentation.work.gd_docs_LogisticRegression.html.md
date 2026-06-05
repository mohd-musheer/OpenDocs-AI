
# Logistic Regression - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/LogisticRegression.html

Algorithm
Logistic Regression
Description
A generalized linear model used for binary classification. It estimates the parameters of a logistic model using iterative optimization. Our implementation uses a raw C++ full-batch Gradient Descent optimizer with an inlined sigmoid activation function for maximum throughput. It handles large datasets by processing the entire batch in memory (or chunks if extended) and updates weights based on the gradient of the Log-Likelihood.
$$ J(\theta) = -\frac{1}{m} \sum_{i=1}^m [y^{(i)}\log(h_\theta(x^{(i)})) +
(1-y^{(i)})\log(1-h_\theta(x^{(i)}))] $$
Algorithm Workflow
START
Initialize weight vector $\mathbf{w}$ and bias $b$ to zeros.
EPOCH LOOP
Iterate for a fixed set of `epochs`.
LINEAR
Compute linear response $z_i = \mathbf{w}^T \mathbf{x}_i + b$ for all
samples.
ACTIVATE
Apply Sigmoid function $p_i = \frac{1}{1 + e^{-z_i}}$.
ERROR
Compute prediction error $e_i = p_i - y_i$.
GRADIENT
Calculate $\nabla w = X^T (\hat{y} - y)$ accumulating over all
samples.
UPDATE
Apply update rule $\mathbf{w} \leftarrow \mathbf{w} - \eta \nabla w$
(where $\eta$ is learning rate).
CONVERGE
Repeat until max epochs.
PREDICT
Return 1 if $p_i > 0.5$ else 0.
Implementation Details
Implemented in `LogisticRegression.cpp`.
for(int e=0; e<epochs; e++){
double z = dot_product(row, coef) + intercept;
double p = 1.0 / (1.0 + exp(-z));
// Gradient update
coef += learning_rate * (y - p) * row;
}
Complexity & Optimization
Time Complexity
O(Epochs * N * P).
Space Complexity
O(P).
Optimizations
Sigmoid inline.
Limitations
Linear boundary.
Use Cases
Binary classification.
