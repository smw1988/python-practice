from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])

        n = len(nums)
        for k in range(1, n + 1):
            self._combine(n, k, 0, 0, nums, result, [None] * k)

        return result


    def _combine(self, n, k, depth, start, nums: List[int], result, current: List[int]):
        if k == 0:
            result.append(current.copy())
        else:
            for i in range(start, n - k + 1):
                current[depth] = nums[i]
                self._combine(n, k - 1, depth + 1, i + 1, nums, result, current)

def test(sln, nums):
    result = sln.subsets(nums)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [1])
    test(sln, [1, 2])
    test(sln, [1, 2, 3])
    test(sln, [3, 2, 1])