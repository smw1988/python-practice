from typing import Iterable, List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        count = len(heights)

        leftSmallerNumbers = [-1] * count
        rightSmallerNumbers = [count] * count

        self._calculateSmallerNumbers(heights, range(count), rightSmallerNumbers)
        self._calculateSmallerNumbers(heights, range(count - 1, -1, -1), leftSmallerNumbers)

        # print(leftSmallerNumbers)
        # print(rightSmallerNumbers)

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

def test(sln, heights):
    result = sln.largestRectangleArea(heights)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [2,1,5,6,2,3])
    test(sln, [2,4])