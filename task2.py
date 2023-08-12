class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        gap_num = {}

        for i in range(m):
            for j in range(n):
                if i - j in gap_num and gap_num[i - j] != matrix[i][j]:
                    return False
                gap_num[i - j] = matrix[i][j]

        return True