from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowCount = len(matrix); columnCount = len(matrix[0])

        rows = set()
        columns = set()

        for i in range(rowCount):
            for j in range(columnCount):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        for i in rows:
            for j in range(columnCount):
                matrix[i][j] = 0

        for j in columns:
            for i in range(rowCount):
                matrix[i][j] = 0

def test(sln, matrix):
    sln.setZeroes(matrix)
    print(matrix)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [[1,1,1],[1,0,1],[1,1,1]])
    test(sln, [[0,1,2,0],[3,4,5,2],[1,3,1,5]])