from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        (rows, columns) = (len(matrix), len(matrix[0]))
        (topBound, bottomBound, leftBound, rightBound) = (-1, rows, -1, columns)
        count = 0

        (xPos, yPos) = (0, 0)
        direction = 1
        while (count < rows * columns):
            if direction == 1: # right
                result.extend([matrix[xPos][j] for j in range(yPos, rightBound)])
                topBound = xPos
                count += (rightBound - yPos)
                (xPos, yPos) = (xPos + 1, rightBound - 1)
                direction = 2
            elif direction == -1: # left
                result.extend([matrix[xPos][j] for j in range(yPos, leftBound, -1)])
                bottomBound = xPos
                count += (yPos - leftBound)
                (xPos, yPos) = (xPos - 1, leftBound + 1)
                direction = -2
            elif direction == 2: # down
                result.extend([matrix[i][yPos] for i in range(xPos, bottomBound)])
                rightBound = yPos
                count += (bottomBound - xPos)
                (xPos, yPos) = (bottomBound - 1, yPos - 1)
                direction = -1
            else: # up
                result.extend([matrix[i][yPos] for i in range(xPos, topBound, -1)])
                leftBound = yPos
                count += (xPos - topBound)
                (xPos, yPos) = (topBound + 1, yPos + 1)
                direction = 1
            
        return result

def test(sln, matrix):
    result = sln.spiralOrder(matrix)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    test(sln, [[1,2,3],[4,5,6],[7,8,9]])
    test(sln, [[1]])