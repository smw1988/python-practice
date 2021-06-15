from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 0):
            return [-1, -1]

        low = 0
        high = len(nums) - 1

        while (low <= high):
            if (low == high):
                if (nums[low] == target):
                    return [low, high]
                else:
                    break
            
            mid = (low + high) // 2
            midValue = nums[mid]
            if (midValue == target):
                lowerBound = mid
                upperBound = mid
                if (mid - 1 >= low and nums[mid - 1] == target):
                    lowerBound = self.findLowerBound(nums, low, mid - 1, target)
                if (mid + 1 <= high and nums[mid + 1] == target):
                    upperBound = self.findUpperBound(nums, mid + 1, high, target)
                return [lowerBound, upperBound]

            if (target < midValue):
                high = mid - 1
            else:
                low = mid + 1

        return [-1, -1]

    def findLowerBound(self, nums: List[int], low: int, high: int, target: int):
        lowerBound = high
        while (low <= high):
            if (low == high):
                if (nums[low] == target):
                    return low
                else:
                    break
            
            mid = (low + high) // 2
            midValue = nums[mid]
            if (midValue == target):
                lowerBound = mid
                high = mid - 1
            else:
                low = mid + 1

        return lowerBound

    def findUpperBound(self, nums: List[int], low: int, high: int, target: int):
        upperBound = low
        while (low <= high):
            if (low == high):
                if (nums[high] == target):
                    return high
                else:
                    break

            mid = (low + high) // 2
            midValue = nums[mid]
            if (midValue == target):
                upperBound = mid
                low = mid + 1
            else:
                high = mid - 1

        return upperBound

def test(sln, nums, target):
    result = sln.searchRange(nums, target)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [5,7,7,8,8,10], 8)
    test(sln, [5,7,7,8,8,10], 6)
    test(sln, [1, 1, 1, 1, 1, 1, 2], 1)