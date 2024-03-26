import numpy as np


def rotvec2matrix(vec, degrees=False) -> np.ndarray:
    # TODO: your code here
    # 利用罗德里格旋转公式返回轴角表示对应的旋转矩阵
    raise NotImplementedError


def matrix2rotvec(matrix) -> np.ndarray:
    angle = np.arccos((np.trace(matrix) - 1) / 2)
    u = np.array(
        [
            matrix[2, 1] - matrix[1, 2],
            matrix[0, 2] - matrix[2, 0],
            matrix[1, 0] - matrix[0, 1],
        ]
    ) / (2 * np.sin(angle))
    return u * angle


def direct_lerp(a, b, t) -> np.ndarray:
    # TODO: your code here
    # 返回使用轴角表示直接插值的结果
    raise NotImplementedError


def rel_lerp(a, b, t) -> np.ndarray:
    # TODO: your code here
    # 返回使用轴角表示相对插值的结果
    raise NotImplementedError