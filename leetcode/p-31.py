from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if (len(nums) == 1):
            return
        
        self.permute(nums)
        return None

    def permute(self, nums: List[int]):
        length = len(nums)
        start = next((x for x in range(length - 2, -1, -1) if nums[x] < nums[x + 1]), None)
        if (start == None):
            self.reverse(nums, 0, length - 1)
        else:
            substitute = next((x for x in range(length - 1, start, -1) if nums[start] < nums[x]), None)
            self.swap(nums, start, substitute)
            self.reverse(nums, start + 1, length - 1)

        return None

    def reverse(self, nums, low, high):
        while (low < high):
            self.swap(nums, low, high)
            low += 1
            high -= 1

    def swap(self, nums, x, y):
        t = nums[x]
        nums[x] = nums[y]
        nums[y] = t

def test(sln, nums):
    sln.nextPermutation(nums)
    print(nums)

if __name__ == "__main__":
    sln = Solution()
    nums = [1, ]
    for iter in range(0, 30):
        sln.nextPermutation(nums)
        print(nums)