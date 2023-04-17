Here is the code written in Python 3 to test Gimbal effect mathematically, based onb the theorital work here mention in this repo:

```python
import numpy as np


def rodrigues_rotation(axis, theta):
    # Based on Rodrigues' Rotation Formula
    axis = np.array(axis).reshape(3, 1)
    rx, ry, rz = axis[:, 0]
    M = np.array([
        [0, -rz, ry],
        [rz, 0, -rx],
        [-ry, rx, 0]
    ])
    R = np.eye(4)
    R[:3, :3] = np.cos(theta) * np.eye(3) +   \
        (1 - np.cos(theta)) * axis @ axis.T + \
        np.sin(theta) * M
    return R


# Rotate via Z axis for 30 degrees
res = rodrigues_rotation([0, 0, 1], 30 / 180 * np.pi)
# print(res)

################################################################


def eular_rotate(rx=0.3, ry=0, rz=0):
    np.set_printoptions(precision=3, suppress=True)
    Rx = rodrigues_rotation([1, 0, 0], rx)
    Ry = rodrigues_rotation([0, 1, 0], ry)
    Rz = rodrigues_rotation([0, 0, 1], rz)
    return Rz @ Ry @ Rx


test1 = eular_rotate(np.pi / 4, np.pi / 2, 0)
test2 = eular_rotate(0, np.pi / 2, np.pi / 4)
print(test1)
print(test2)

``` 