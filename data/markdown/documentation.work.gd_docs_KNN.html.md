
# K-Nearest Neighbors - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/KNN.html

Algorithm
K-Nearest Neighbors
Description
A non-parametric, lazy learning algorithm that does not 'learn' a fixed model but instead stores the training instances. Prediction is performed by searching for the k most similar instances in the feature space. Our implementation is optimized for dense vectors using efficient Euclidean distance calculations and C++ standard library partial sorting to find the top-k neighbors without sorting the entire dataset.
$$ d(\mathbf{p}, \mathbf{q}) = \sqrt{ \sum_{i=1}^n (q_i - p_i)^2 } $$
Algorithm Workflow
TRAINING
Store the entire dataset $X_{train}$ and $y_{train}$ in
memory.
QUERY
For each new sample $x_{q}$ to predict:
DISTANCE
Compute Squared Euclidean Distance $d(x_q, x_i)$ for all
$i=1..N$.
SEARCH
Use `std::partial_sort` to find the $k$ smallest distances in $O(N
\log K)$ time.
RETRIEVE
Get the labels of these $k$ nearest neighbors.
VOTE
For Classification, assign the most frequent class (Mode).
AVERAGE
For Regression, assign the mean value of the neighbors.
END
Return the predicted value.
Implementation Details
Implemented in `KNN.cpp`.
// Partial sort to find top-k
std::partial_sort(indices.begin(), indices.begin()+k, indices.end(),
[&](int i, int j){ return dists[i] < dists[j]; });
// Vote
for(int i=0; i<k; ++i) votes[y[indices[i]]]++;
Complexity & Optimization
Time Complexity
Pred: O(N * P).
Space Complexity
O(N * P).
Optimizations
Partial Sort.
Limitations
Slow prediction.
Use Cases
Pattern recognition.
