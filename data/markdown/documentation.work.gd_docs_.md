
# VectorForgeML Documentation - API Reference, Guides & 30+ Algorithm Docs

URL: https://documentation.work.gd/docs/

VectorForgeML Documentation
Usage guides, API references, and examples for the VectorForgeML machine learning framework. Built on C++ for maximum performance in R.
Quick Start Guide
Get up and running with a simple classification pipeline in VectorForgeML.
First, install VectorForgeML, then build your first pipeline:
library(VectorForgeML)
# Load data
data(iris)
# Create pipeline
pipe <- Pipeline(steps = list(
c("scaler", StandardScaler()),
c("model", SoftmaxRegression())
))
# Train
pipe$fit(iris[, 1:4], iris[, 5])
API Reference
Explore the available modules and algorithms in VectorForgeML.
