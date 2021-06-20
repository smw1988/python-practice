from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix: List[List[int]] = [[None] * n for _ in range(0, n)]

        (topBound, bottomBound, leftBound, rightBound) = (-1, n, -1, n)

        (xPos, yPos) = (0, 0)
        direction = 1
        value = 1
        while (value <= n * n):
            if direction == 1: # right
                for j in range(yPos, rightBound):
                    matrix[xPos][j] = value
                    value += 1
                topBound = xPos
                (xPos, yPos) = (xPos + 1, rightBound - 1)
                direction = 2
            elif direction == -1: # left
                for j in range(yPos, leftBound, -1):
                    matrix[xPos][j] = value
                    value += 1
                bottomBound = xPos
                (xPos, yPos) = (xPos - 1, leftBound + 1)
                direction = -2
            elif direction == 2: # down
                for i in range(xPos, bottomBound):
                    matrix[i][yPos] = value
                    value += 1
                rightBound = yPos
                (xPos, yPos) = (bottomBound - 1, yPos - 1)
                direction = -1
            else: # up
                for i in range(xPos, topBound, -1):
                    matrix[i][yPos] = value
                    value += 1
                leftBound = yPos
                (xPos, yPos) = (topBound + 1, yPos + 1)
                direction = 1
            
        return matrix

def test(sln, n):
    result = sln.generateMatrix(n)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, 1)