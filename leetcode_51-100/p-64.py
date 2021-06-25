from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        row0 = grid[0]
        columns = len(row0)

        for i in range(1, columns):
            row0[i] += row0[i - 1]
        
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, rows):
            for j in range(1, columns):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[rows - 1][columns - 1]

def test(sln, grid):
    result = sln.minPathSum(grid)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [[1,3,1],[1,5,1],[4,2,1]])
    test(sln, [[1,2,3],[4,5,6]])