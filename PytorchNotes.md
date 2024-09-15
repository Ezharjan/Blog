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
5. torch.sum为求和：
   ```python
    import torch
    # 创建一个二维张量
    a = torch.tensor([[2, 3, 5], [1, 4, 9]])    
    # 计算所有元素的总和
    total_sum = torch.sum(a)
    print("总和:", total_sum)  # 输出: tensor(24)   
    # 沿列求和
    sum_dim0 = torch.sum(a, dim=0)
    print("沿列求和:", sum_dim0)  # 输出: tensor([3, 7, 14])    
    # 沿行求和
    sum_dim1 = torch.sum(a, dim=1)
    print("沿行求和:", sum_dim1)  # 输出: tensor([10, 14])
   ```
6. 