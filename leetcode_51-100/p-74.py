from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix); columns = len(matrix[0])
        size = rows * columns

        low = 0; high = size - 1
        while (low <= high):
            if low == high:
                return Solution._getValue(matrix, low, columns) == target

            mid = (low + high) // 2
            midValue = Solution._getValue(matrix, mid, columns)
            if midValue == target:
                return True
            elif midValue < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def _getValue(matrix, index: int, columns: int):
        return matrix[index // columns][index % columns]

def test(sln, matrix, target):
    result = sln.searchMatrix(matrix, target)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    test(sln, [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)