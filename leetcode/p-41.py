# Input: nums = [1,2,0]
# Output: 3

# Input: nums = [3,4,-1,1]
# Output: 2

# Input: nums = [7,8,9,11,12]
# Output: 1

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        currentPos = 0
        size = len(nums)

        while (currentPos < size):
            n = nums[currentPos]
            rightPos = n - 1

            if (0 <= rightPos < currentPos):
                nums[rightPos] = n
                currentPos += 1
            elif (currentPos < rightPos < size):
                t = nums[currentPos]
                nums[currentPos] = nums[rightPos]
                nums[rightPos] = t
            else:
                currentPos += 1

        for i in range(0, size):
            if nums[i] != i + 1:
                return i + 1

        return size + 1

def test(sln, nums):
    result = sln.firstMissingPositive(nums)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [1,2,0])
    test(sln, [3,4,-1,1])
    test(sln, [7,8,9,11,12])