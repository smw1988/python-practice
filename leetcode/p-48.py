from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if (n == 1):
            return None

        for row in range(0, n // 2):
            for column in range(row, n - 1 - row):
                self.rotateCorner(matrix, row, column, n)

        return None

    def rotateCorner(self, mat: List[List[int]], i: int, j: int, n: int):
        t = mat[i][j]
        m = n - 1
        mat[i][j] = mat[m - j][i]
        mat[m - j][i] = mat[m - i][m - j]
        mat[m - i][m - j] = mat[j][m - i]
        mat[j][m - i] = t

def test(sln, matrix):
    sln.rotate(matrix)
    print(matrix)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [[1,2,3],[4,5,6],[7,8,9]])
    test(sln, [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
    test(sln, [[1]])
    test(sln, [[1,2],[3,4]])