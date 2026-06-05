
# Softmax Regression - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/SoftmaxRegression.html

Algorithm
Softmax Regression
Description
An extension of Logistic Regression to multi-class problems. It models the probability that a sample belongs to a specific class k using the Softmax function. The implementation relies on the 'Log-Sum-Exp' trick to prevent numerical instability (overflow/underflow) during the exponentiation step. This is critical for stable training on datasets with unscaled features.
$$ P(y=j|\mathbf{x}) = \frac{e^{\mathbf{w}_j^T \mathbf{x}}}{\sum_{k=1}^K e^{\mathbf{w}_k^T
\mathbf{x}}} $$
Algorithm Workflow
START
Identify $K$ unique classes and initialize $W$ matrix ($P \times
K$).
EPOCH LOOP
Iterate through optimization steps.
LOGITS
Compute raw scores $Z = XW$.
MAX TRICK
Find $M = \max(Z)$ for numerical stability.
PROBABILITIES
Compute Softmax $P(k|x) = \exp(Z_k - M) / \sum \exp(Z_j - M)$.
LOSS GRAD
Compute gradients $\nabla W$ based on Cross-Entropy Loss.
UPDATE
Adjust weights $W \leftarrow W - \eta \nabla W$.
END
Return trained weights for $K$ classes.
Implementation Details
Implemented in `SoftmaxRegression.cpp`.
// Softmax with Log-Sum-Exp trick
double max_z = max(logits);
double sum_exp = 0;
for(double z : logits) sum_exp += exp(z - max_z);
probs[k] = exp(logits[k] - max_z) / sum_exp;
Complexity & Optimization
Time Complexity
O(Epochs * N * P * K).
Space Complexity
O(P * K).
Optimizations
Log-Sum-Exp stability.
Limitations
Linear boundaries.
Use Cases
Multiclass classification.
