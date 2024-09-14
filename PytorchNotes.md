# Pytorch 笔记

1. 张量：单/多维矩阵的学名。
2. torch.Size([2,3]): 一个2x3的2D Matrix；torch.Size([2,3,4])：一个2x3x4的3D Matrix；……
3. torch.matmul(x, y)：x、y矩阵的乘积。
4. 在 Python 中，可以使用 NumPy 或 PyTorch 来定义张量，用prod函数求所有元素的乘积（张量权重）：
    ```
    import numpy as np
    a = np.array([[2, 3, 5, 7], [1, 4, 9, 8], [2, 3, 5, 4]]) 
    prod_result = np.prod(a)
    print("所有元素的乘积:", prod_result)
    OR
    import torch
    a = torch.tensor([[2, 3, 5, 7], [1, 4, 9, 8], [2, 3, 5, 4]])
    print(a)
    prod_result = tensor.prod(a)
    print("所有元素的乘积:", prod_result)
    ```
5. 