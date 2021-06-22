from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)

        if (size == 0):
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        if newInterval[0] > intervals[size - 1][1]:
            intervals.append(newInterval)
            return intervals

        if newInterval[0] <= intervals[0][0] and newInterval[1] >= intervals[size - 1][1]:
            return [newInterval]

        leftBoundPos = self.findInsertPos(intervals, newInterval[0])
        rightBoundPos = self.findInsertPos(intervals, newInterval[1])

        if (leftBoundPos == rightBoundPos):
            if leftBoundPos % 2 == 0:
                intervals.insert(leftBoundPos // 2, newInterval)
        else:
            leftBound = min(newInterval[0], intervals[leftBoundPos // 2][0])
            rightBound = max(newInterval[1], intervals[(rightBoundPos + 1) // 2 - 1][1])

            leftIndex = leftBoundPos // 2
            rightIndex = (rightBoundPos + 1) // 2

            intervals[leftIndex: rightIndex] = [[leftBound, rightBound]]

        return intervals

    def findInsertPos(self, intervals: List[List[int]], k: int):
        (low, high) = (0, len(intervals) * 2)

        while (low <= high):
            if low == high:
                return low

            mid = (low + high) // 2
            if mid % 2 == 0:
                leftBound = -100000000 if mid == 0 else intervals[mid // 2 - 1][1]
                rightBound = 100000000 if mid == len(intervals) * 2 else intervals[mid // 2][0]

                if leftBound < k < rightBound:
                    return mid
                elif k <= leftBound:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                interval = intervals[mid // 2]
                if interval[0] <= k <= interval[1]:
                    return mid
                elif (k < interval[0]):
                    high = mid - 1
                else:
                    low = mid + 1

def test(sln, intervals, newInterval):
    result = sln.insert(intervals, newInterval)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [[1,3],[6,9]], [2,5])
    test(sln, [[1,2],[3,5],[6,7],[8,10],[12,16]], [10,24])
    test(sln, [], [5,7])
    test(sln, [[1,5]], [2,3])
    test(sln, [[1,5]], [2,7])
    test(sln, [[1,5],[6,8]], [5,6])