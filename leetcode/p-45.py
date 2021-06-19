from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 0

        steps = [-1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            jumpLen = nums[i]
            if (jumpLen == 0):
                continue

            if (jumpLen + i >= len(nums) - 1):
                steps[i] = 1
                continue
            
            minJump = 1000000
            for j in range(1, jumpLen + 1):
                if steps[i + j] != -1:
                    minJump = min(minJump, steps[i + j])
            if minJump != 1000000:
                steps[i] = minJump + 1

        return steps[0]

def test(sln, nums):
    result = sln.jump(nums)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [2,3,1,1,4])
    test(sln, [2,3,0,1,4])
    test(sln, [1,1,1,1])