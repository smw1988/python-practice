from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while (low <= high):
            if (low == high):
                if (target == nums[low]):
                    return low
                if (target < nums[low]):
                    return low
                else:
                    return low + 1
            
            mid = (low + high) // 2
            midValue = nums[mid]

            if (midValue == target):
                return mid
            if (target < midValue):
                high = mid - 1
            else:
                low = mid + 1

        return low

def test(sln, nums, target):
    result = sln.searchInsert(nums, target)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    # test(sln, [1,3,5,6], 5)
    # test(sln, [1,3,5,6], 2)
    # test(sln, [1,3,5,6], 7)
    # test(sln, [1,3,5,6], 0)
    test(sln, [1, 3], 0)