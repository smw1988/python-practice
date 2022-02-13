from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        startOf1 = -1
        startOf2 = len(nums)
        current = 0

        while current < startOf2:
            value = nums[current]
            if value == 0:
                if startOf1 != -1:
                    Solution._swap(nums, startOf1, current)
                    startOf1 += 1
                current += 1
            elif value == 1:
                if startOf1 == -1:
                    startOf1 = current
                current += 1
            else:
                startOf2 -= 1
                Solution._swap(nums, current, startOf2)
                

    def _swap(nums: List[int], i: int, j: int):
        t = nums[i]; nums[i] = nums[j]; nums[j] = t

def test(sln, nums):
    sln.sortColors(nums)
    print(nums)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [2,0,2,1,1,0])
    test(sln, [2,0,1])
    test(sln, [0])
    test(sln, [1])
    test(sln, [2,2,2,0,0])
    test(sln, [1,1,0,0])