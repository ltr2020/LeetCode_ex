class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import numpy as np
        matrix[:] = np.array(matrix)
        matrix[:] = np.flipud(matrix).T.tolist()
        return matrix