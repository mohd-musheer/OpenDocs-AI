
# Accuracy Score - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/accuracy_score.html

Algorithm
Accuracy Score
Description
The Accuracy Score is a fundamental classification metric that computes the ratio of correctly predicted observations to the total observations. It is defined as $(TP+TN)/(TP+TN+FP+FN)$. While intuitive, it may be misleading for imbalanced datasets, where high accuracy can be achieved by simply predicting the majority class.
$$ \text{Accuracy} = \frac{1}{n} \sum_{i=1}^{n} 1(y_i = \hat{y}_i) $$
Use Cases
Balanced Classification
