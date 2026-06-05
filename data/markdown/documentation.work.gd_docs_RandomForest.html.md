
# Random Forest - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/RandomForest.html

Algorithm
Random Forest
Description
A robust ensemble meta-estimator that fits a number of decision tree classifiers/regressors on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. Our implementation utilizes `std::vector` and raw pointers for managing a forest of trees, with specific optimizations for random feature selection at each node split.
$$ \hat{y}(x) = \frac{1}{T} \sum_{t=1}^T f_t(x) $$
Algorithm Workflow
START
Initialize the forest with `ntrees` empty trees.
BOOTSTRAP
For each tree t=1..T, generate a random sample of size N from X with
replacement.
BUILD
Grow a decision tree on the bootstrapped data.
FEATURE SUBSET
At each node, select a random subset of features of size
`mtry`.
BEST SPLIT
Find the best split among the `mtry` features only.
GROW
Continue splitting until max_depth is reached (no pruning).
STORE
Save the root pointer of the tree in the forest container.
PREDICT
For a new sample, traverse all T trees.
AGGREGATE
Compute the average (Regression) or Majority Vote (Classification) of
all tree predictions.
END
Return the final ensemble prediction.
Implementation Details
Implemented in `RandomForest.cpp`.
for(int i=0; i<ntrees; ++i) {
// Bootstrap sampling
// Random feature selection
trees[i] = build_tree(bootstrap_X, bootstrap_y, mtry);
}
// Prediction
for(Node* t : trees)
preds += predict_tree(t, X);
preds /= ntrees;
Complexity & Optimization
Time Complexity
Training: O(T * N * log(N) * mtry).
Space Complexity
O(T * Nodes).
Optimizations
Ensemble variance reduction.
Limitations
Single-threaded build.
Use Cases
Robust classification/regression.
