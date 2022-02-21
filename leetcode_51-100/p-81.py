from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return self._search(nums, target, 0, len(nums) - 1)

    def _search(self, nums: List[int], target: int, low: int, high: int) -> bool:
        while low <= high:
            if low == high:
                return nums[low] == target

            mid = (low + high) // 2
            midValue = nums[mid]

            if midValue == target:
                return True

            if nums[low] == midValue == nums[high]:
                return self._search(nums, target, low, mid - 1) or self._search(nums, target, mid + 1, high)

            if nums[low] <= midValue:
                if nums[low] <= target <= midValue:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if midValue <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False


def test(sln, nums, target):
    result = sln.search(nums, target)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [2,5,6,0,0,1,2], 0)
    test(sln, [2,5,6,0,0,1,2], 3)
    test(sln, [0,1], 0)
    test(sln, [0,1], 1)
    test(sln, [1,0], 0)
    test(sln, [1,0], 1)
    test(sln, [1,1,1], 1)
    test(sln, [1,1,1,1], 1)
    test(sln, [1,1,1], 0)
    test(sln, [1,1,1,1], 0)
    test(sln, [1,2,3,0,0,0,0], 0)
    test(sln, [1,2,3,0,0,0,0], 2)
    test(sln, [4,4,4,4,1,2,3], 4)
    test(sln, [4,4,4,4,1,2,3], 2)
    test(sln, [1,0,1,1,1], 0)
    test(sln, [1,0,1,1,1,1,1], 0)
    test(sln, [1,1,0,1,1,1,1], 0)