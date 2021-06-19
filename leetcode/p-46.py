from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.doPermute(nums, result, 0)
        return result

    def doPermute(self, nums: List[int], result: list, depth: int):
        if depth == len(nums):
            result.append(nums.copy())
            return
        
        for j in range(depth, len(nums)):
            self.swap(nums, depth, j)
            self.doPermute(nums, result, depth + 1)
            self.swap(nums, depth, j)

    def swap(self, nums: list, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

def test(sln, nums):
    result = sln.permute(nums)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [1])