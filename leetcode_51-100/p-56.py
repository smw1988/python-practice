from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        intervals.sort(key=lambda i: i[0])

        workingInterval = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            mergedInterval = self.mergeInterval(workingInterval, interval)

            if mergedInterval == None:
                result.append(workingInterval)
                workingInterval = interval
            else:
                workingInterval = mergedInterval

        result.append(workingInterval)

        return result

    def mergeInterval(self, a: list, b: list):
        if a[1] < b[0] or b[1] < a[0]:
            return None
        return [min(a[0], b[0]), max(a[1], b[1])]

def test(sln, intervals):
    result = sln.merge(intervals)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [[1,3],[2,6],[8,10],[15,18]])
    test(sln, [[1,4],[4,5]])
    test(sln, [[1,2]])