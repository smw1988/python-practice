from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        nums = self.removeDuplicate(nums)
        triples = set()

        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    lValue = target - nums[i] - nums[j] - nums[k]
                    l = self.search(nums, k + 1, len(nums) - 1, lValue)
                    if (l > 0):
                        triples.add((nums[i], nums[j], nums[k], nums[l]))

        return list(triples)

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
                if (repeat <= 4):
                    result.append(n)

        return result

    def search(self, nums: List[int], low: int, high: int, value: int) -> int:
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] == value):
                return mid
            elif (nums[mid] > value):
                high = mid - 1
            else:
                low = mid + 1
        return 0


if __name__ == "__main__":
    s = Solution()
    nums = [2,2,2,2,2]
    #[1,0,-1,0,-2,2]
    
    result = s.fourSum(nums, 8)
    print(result)