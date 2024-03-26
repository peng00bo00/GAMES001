import numpy as np


class Quaternion:
    # (w, ix, jy, kz)
    def __init__(self, quat=[0, 1, 0, 0]) -> None:
        self.quat = self.normalize(quat)

    def normalize(self, quat) -> np.ndarray:
        return quat / np.linalg.norm(quat)

    def to_matrix(self) -> np.ndarray:
        w, x, y, z = self.quat
        return np.array(
            [
                [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)],
            ]
        )

    def from_rotvec(self, vec):
        vec = np.array(vec)
        angle = np.linalg.norm(vec)
        self.quat = np.array([np.cos(angle / 2), *np.sin(angle / 2) * vec / angle])
        return self

    def __mul__(self, other):
        # TODO: your code here
        # 返回两个四元数的乘积
        raise NotImplementedError

    @staticmethod
    def Nlerp(a, b, t) -> "Quaternion":
        # TODO: your code here
        # 返回 Nlerp 插值结果
        raise NotImplementedError

    @staticmethod
    def Slerp(a, b, t, short_path=True) -> "Quaternion":
        # TODO: your code here
        # short_path 为 True 时，返回最小弧的 Slerp 插值结果
        # 返回 Slerp 插值结果
        raise NotImplementedError