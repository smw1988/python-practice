from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        largest = -1000000

        for n in nums:
            if (n > largest):
                largest = n
                nums[index] = n
                index += 1

        return index

if __name__ == "__main__":
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = s.removeDuplicates(nums)
    print(k)
    print(nums)