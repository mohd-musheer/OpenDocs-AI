
# K-Means Clustering - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/KMeans.html

Algorithm
K-Means Clustering
Description
An iterative unsupervised learning algorithm that partitions a dataset into K distinct, non-overlapping subgroups (clusters). Each data point belongs to the cluster with the nearest mean. The algorithm minimizes the within-cluster sum of squares (WCSS). It employs the classic Lloyd's algorithm with efficient C++ loops for distance calculation and centroid updates.
$$ \text{arg} \min_S \sum_{i=1}^k \sum_{\mathbf{x} \in S_i} ||\mathbf{x} - \mathbf{\mu}_i||^2 $$
Algorithm Workflow
START
Specify $K$ clusters.
INIT
Randomly select $K$ data points as initial centroids
$\mu^{(0)}$.
ASSIGN
For every point $x_i$, find the nearest centroid $c_j$ minimizing
$||x_i - \mu_j||^2$.
UPDATE
Recalculate each centroid $\mu_j$ as the mean of all points assigned
to it.
CHECK
If centroids have not changed (or change < epsilon), STOP.
LOOP
Otherwise, repeat the Assign and Update steps.
END
Return cluster labels and final centroid locations.
Implementation Details
Implemented in `KMeans.cpp`.
while(changed && iter < max_iter) {
// Assignment
int c = nearest_centroid(row, centroids);
// Update
new_centroids[c] += row;
counts[c]++;
}
Complexity & Optimization
Time Complexity
O(I * N * K * P).
Space Complexity
O(K * P).
Optimizations
In-place updates.
Limitations
Local optima.
Use Cases
Clustering.
