from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while (low <= high):
            if (low == high):
                return low if nums[low] == target else -1
            
            mid = (low + high) // 2

            midValue = nums[mid]
            if (midValue == target):
                return mid

            if (midValue >= nums[low]):
                if (target >= nums[low] and target <= midValue):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if (target >= midValue and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


def test(sln, nums, target):
    result = sln.search(nums, target)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [4,5,6,7,0,1,2], 0)
    test(sln, [4,5,6,7,0,1,2], 3)
    test(sln, [0, 1], 0)
    test(sln, [0, 1], 1)
    test(sln, [1, 0], 0)
    test(sln, [1, 0], 1)