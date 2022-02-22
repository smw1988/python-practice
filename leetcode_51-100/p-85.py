from typing import Iterable, List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heightMatrix: List[List[int]] = self._processMatrix(matrix)
        maxRectArea = max((self._largestRectangleArea(row) for row in heightMatrix))
        return maxRectArea
        return 0

    def _processMatrix(self, matrix: List[List[str]]):
        rows = len(matrix); columns = len(matrix[0])
        heightMatrix = [[0] * columns for _ in range(rows)]

        heightMatrix[0] = [1 if e == "1" else 0 for e in matrix[0]]

        for i in range(1, rows):
            for j in range(columns):
                if matrix[i][j] == "1":
                    heightMatrix[i][j] = heightMatrix[i - 1][j] + 1

        return heightMatrix

    def _largestRectangleArea(self, heights: List[int]) -> int:
        count = len(heights)

        leftSmallerNumbers = [-1] * count
        rightSmallerNumbers = [count] * count

        self._calculateSmallerNumbers(heights, range(count), rightSmallerNumbers)
        self._calculateSmallerNumbers(heights, range(count - 1, -1, -1), leftSmallerNumbers)

        areaFunc = lambda i: heights[i] * (rightSmallerNumbers[i] - leftSmallerNumbers[i] - 1)
        maxRectArea = max((areaFunc(i) for i in range(count)))

        return maxRectArea

    def _calculateSmallerNumbers(self, heights: List[int], indices: Iterable[int], results: List[int]):
        stack = []
        for i in indices:
            h = heights[i]
            while len(stack) > 0:
                top = stack[len(stack) - 1]
                if h < top[1]:
                    results[top[0]] = i
                    stack.pop()
                else:
                    break
            
            stack.append((i, h))

def test(sln, matrix):
    result = sln.maximalRectangle(matrix)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    test(sln, [["0"]])
    test(sln, [["1"]])