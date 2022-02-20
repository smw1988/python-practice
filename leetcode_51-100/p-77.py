from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        result = []
        current = [None] * k
        self._combine(n, k, 0, 0, result, current)

        return result

    def _combine(self, n, k, depth, start, result, current: List[int]):
        if k == 0:
            result.append(current.copy())
        else:
            for i in range(start, n - k + 1):
                current[depth] = i + 1
                self._combine(n, k - 1, depth + 1, i + 1, result, current)

def test(sln, n, k):
    result = sln.combine(n, k)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, 4, 2)
    test(sln, 1, 1)
    test(sln, 3, 1)
    test(sln, 4, 4)