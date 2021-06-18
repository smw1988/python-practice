from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length == 0:
            return 0

        leftHeight = self.calculate(height, range(0, length))
        rightHeight = self.calculate(height, range(length - 1, -1, -1))

        print(leftHeight)
        print(rightHeight)

        result = 0
        for i in range(0, length):
            result += min(leftHeight[i], rightHeight[i])

        return result

    def calculate(self, height, indexList):
        result = [None] * len(indexList)

        heighest = 0
        for i in indexList:
            h = height[i]
            if (h < heighest):
                result[i] = heighest - h
            else:
                heighest = h
                result[i] = 0
        
        return result

def test(sln, height):
    result = sln.trap(height)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [0,1,0,2,1,0,1,3,2,1,2,1])