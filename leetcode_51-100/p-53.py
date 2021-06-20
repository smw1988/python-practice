from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        f = [nums[0]] * size
        g = [nums[0]] * size

        for i in range(1, size):
            g[i] = max(nums[i], nums[i] + g[i - 1])
            f[i] = max(f[i - 1], g[i])

        return f[size - 1]

def test(sln, nums):
    result = sln.maxSubArray(nums)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [-2,1,-3,4,-1,2,1,-5,4])
    test(sln, [1])
    test(sln, [5,4,-1,7,8])
    test(sln, [-2, 1])