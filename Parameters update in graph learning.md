# Parameters update in graph learning.



## What is the drawbacks of using the algorithm below?

Input: User-item bipartite Graph G; graph propagation depth K;
Output: Parameter Θr in graph learning module, Θa in attribute
update module;
1: Random initialize model parameters;
2: l=0;
3: Calculate initial user attribute Xl and Yl (Eq.(3));
4: while not converged do
5: Sample a batch of training data;
6: Update ul and vl (Eq.(1))
7: for k = 0 to K − 1 do
8: Update Ul ,k+1 and Vl ,k+1 (Eq.(7));
9: end for
10: Predict rating preference (Eq.(8))
11: Predict attribute values (Eq.(9))
12: Parameters update according to Eq. (13);
13: Update the approximated attributes Xl+1 and Yl+1 (Eq.
(10));
14: l=l+1;
15: end while
16: Return Θ.

Some potential drawbacks of using this algorithm are:

1. Risk of overfitting: Since the algorithm updates the model parameters based on the training data at every iteration, there is a risk of overfitting the model to the training data, which may lead to poor performance on unseen data.

2. Parameter settings: The performance of the algorithm may be highly dependent on the setting of various hyperparameters, such as the depth of graph propagation, the batch size, and the learning rate. Choosing appropriate settings for these hyperparameters can be challenging and time-consuming.

3. Computationally expensive: The graph propagation step in this algorithm requires multiple updates of the user and item embedding matrices, which can be computationally expensive, especially for large-scale datasets.

4. Lack of interpretability: Since the algorithm involves multiple layers of matrix multiplication and nonlinear activation functions, it can be difficult to interpret the learned model parameters and understand how they relate to the underlying data.