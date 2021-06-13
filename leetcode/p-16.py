from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums = self.removeDuplicate(nums)
        closest = 1000000

        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                kValue = target - nums[i] - nums[j]
                closestCandidate = self.search(nums, j + 1, len(nums) - 1, kValue)
                if (closestCandidate == 0):
                    return target

                if (abs(closestCandidate) < abs(closest)):
                    closest = closestCandidate

        return target + closest

    def removeDuplicate(self, nums: List[int]) -> List[int]:
        result = []

        previous = None
        repeat = 0

        for n in nums:
            if (n != previous):
                previous = n
                repeat = 1
                result.append(n)
            else:
                repeat += 1
                if (repeat <= 3):
                    result.append(n)

        return result

    def search(self, nums: List[int], low: int, high: int, value: int) -> int:
        closestDistance = 1000000

        while (low <= high):
            mid = (low + high) // 2
            if (abs(nums[mid] - value) < abs(closestDistance)):
                closestDistance = nums[mid] - value
                if closestDistance == 0:
                    return 0

            if (nums[mid] > value):
                high = mid - 1
            else:
                low = mid + 1

        return closestDistance


if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,1,55] #[0,0,0] #[-1,2,1,-4]
    target = 3
    result = s.threeSumClosest(nums, target)
    print(result)