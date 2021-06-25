from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        if grid[0][0] == 1: return 0
        
        rows = len(grid)
        row0 = grid[0]
        columns = len(row0)

        blocked = False
        for i in range(0, columns):
            if blocked:
                row0[i] = 0
            elif row0[i] == 0:
                row0[i] = 1
            else:
                row0[i] = 0
                blocked = True
        
        blocked = False
        for i in range(1, rows):
            if blocked:
                grid[i][0] = 0
            elif grid[i][0] == 0:
                grid[i][0] = 1
            else:
                grid[i][0] = 0
                blocked = True

        for i in range(1, rows):
            for j in range(1, columns):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        
        return grid[rows - 1][columns - 1]

def test(sln, obstacleGrid):
    result = sln.uniquePathsWithObstacles(obstacleGrid)
    #print(obstacleGrid)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [[0,0,0],[0,1,0],[0,0,0]])
    test(sln, [[0,1],[0,0]])