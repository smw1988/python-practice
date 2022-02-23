from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = [[]]

        count = len(nums)
        for i in range(1, count + 1):
            self._subsetsWithDup(nums, results, i)

        return results

    def _subsetsWithDup(self, nums: List[int], results: List, size: int):
        tempResult = [None] * size
        self._subset(nums, results, 0, 0, tempResult)

    def _subset(self, nums: List[int], results: List, startIndex: int, resultIndex: int, tempResult: List[int]):
        remainingSelection = len(tempResult) - resultIndex

        if remainingSelection == 0:
            results.append(tempResult.copy())
        else:
            for i in range(startIndex, len(nums) - remainingSelection + 1):
                if i == startIndex or nums[i] != nums[i - 1]:
                    tempResult[resultIndex] = nums[i]
                    self._subset(nums, results, i + 1, resultIndex + 1, tempResult)

def test(sln, nums):
    result = sln.subsetsWithDup(nums)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [1,2,2])
    test(sln, [0])
    test(sln, [1,1,1,2])
    test(sln, [1,3,3,3,4,5,5])