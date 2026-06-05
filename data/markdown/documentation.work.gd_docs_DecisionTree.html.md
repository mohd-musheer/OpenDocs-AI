
# Decision Tree Regressor - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/DecisionTree.html

Decision Tree Regressor
Description
A high-performance, recursive partitioning algorithm that constructs a regression tree by exhaustively searching for optimal splits. Unlike standard implementations, vectorForgeML's Decision Tree is built directly in C++ using raw pointers for graph construction, ensuring minimal memory overhead and cache-friendly traversal. It supports deep trees and handles continuous features with high precision. The model predicts the target value by traversing the tree from root to leaf, where each node represents a decision rule based on a single feature threshold.
Algorithm Workflow
Implementation Details
Implemented in `DecisionTree.cpp`. Recursively partitions data.
Node* build(NumericMatrix X, NumericVector y, int depth,int maxd){
// ... (find best split based on minimizing MSE) ...
if(depth>=maxd || bf==-1){
node->value=s/n; // Leaf node: store mean
return node;
}
node->left=build(XL,yL,depth+1,maxd);
node->right=build(XR,yR,depth+1,maxd);
return node;
}
Complexity & Optimization
Time Complexity
Training: O(N * P * D). Prediction: O(D).
Space Complexity
O(Nodes).
Optimizations
Recursive implementation with index passing.
Limitations
Regression only.
Use Cases
Non-linear regression.
