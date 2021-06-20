from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        if (size == 1):
            return True

        reachable = [False] * size
        reachable[0] = True

        for i in range(0, size):
            if reachable[i]:
                if (i + nums[i] >= size - 1):
                    return True
                for j in range(i + 1, i + nums[i] + 1):
                    reachable[j] = True

        return False

def test(sln, nums):
    result = sln.canJump(nums)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [2,3,1,1,4])
    test(sln, [3,2,1,0,4])