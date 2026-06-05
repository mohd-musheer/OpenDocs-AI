
# Pipeline - VectorForgeML Documentation

URL: https://documentation.work.gd/docs/Pipeline.html

Algorithm
Pipeline
Description
Sequentially apply a list of transforms and a final estimator.
Algorithm Workflow
Iterate transformer steps:
fit_transform()
Final step: fit()
Implementation Details
Implemented in `pipeline.R`.
fit=function(X,y){
data <- X
for(i in seq_len(n_steps)){
step <- steps[[i]]
if(pipeline_is_transformer(step)){
if(pipeline_has_method(step,"fit_transform")){
data <- step$fit_transform(data)
} # ...
} else if(pipeline_is_estimator(step)){
step$fit(data,y)
}
}
}
Use Cases
General purpose.
