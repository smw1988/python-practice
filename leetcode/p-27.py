from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while (left <= right):
            if (nums[left] != val):
                left += 1
            else:
                while (right >= left and nums[right] == val):
                    right -= 1
                if (right >= left):
                    t = nums[left]
                    nums[left] = nums[right]
                    nums[right] = t
                    right -= 1
        return left

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,2,3]
    k = s.removeElement(nums, 3)
    print(k)
    print(nums)