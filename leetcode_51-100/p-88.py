from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        current1 = m - 1; current2 = n - 1
        totalCurrent = m + n - 1

        while current1 >= 0 and current2 >= 0:
            if (nums1[current1] < nums2[current2]):
                nums1[totalCurrent] = nums2[current2]
                current2 -= 1
            else:
                nums1[totalCurrent] = nums1[current1]
                current1 -= 1
            totalCurrent -= 1
        
        while current2 >= 0:
            nums1[totalCurrent] = nums2[current2]
            current2 -= 1
            totalCurrent -= 1

def test(sln, nums1, m, nums2, n):
    sln.merge(nums1, m, nums2, n)
    print(nums1)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [1,2,3,0,0,0], 3, [2,5,6], 3)
    test(sln, [1], 1, [], 0)
    test(sln, [0], 0, [1], 1)
    test(sln, [1,2,3,0,0,0], 3, [4,5,6], 3)
    test(sln, [4,5,6,0,0,0], 3, [1,2,3], 3)