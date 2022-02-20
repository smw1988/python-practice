from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsCount = len(nums)
        lastValue = None
        replaceIndex = 0
        occurrence = 0

        for i in range(numsCount):
            current = nums[i]
            if current == lastValue:
                occurrence += 1
                if occurrence <= 2:
                    nums[replaceIndex] = current
                    replaceIndex += 1
            else:
                lastValue = current
                occurrence = 1
                nums[replaceIndex] = current
                replaceIndex += 1

        return replaceIndex

def test(sln, nums):
    result = sln.removeDuplicates(nums)
    print(result)
    print(nums)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [1,1,1,2,2,3])
    test(sln, [0,0,1,1,1,1,2,3,3])
    test(sln, [1,1,2,2])
    test(sln, [1])