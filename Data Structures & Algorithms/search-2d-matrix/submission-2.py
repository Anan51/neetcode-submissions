class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix) and not (target >= matrix[i][0] and target <= matrix[i][-1]):
            i += 1
        if i >= len(matrix):
            return False
        return target in matrix[i]