from functools import reduce
from operator import __mul__

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        choices = m + n - 2
        selection = min(m, n) - 1
        return self.combination(choices, selection)

    def combination(self, n, k):
        if k == 0: return 1
        return reduce(__mul__, range(n, n - k, -1)) // reduce(__mul__, range(k, 0, -1))

def test(sln, m, n):
    result = sln.uniquePaths(m, n)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, 7, 3)
    test(sln, 3, 7)
    test(sln, 3, 3)
    test(sln, 2, 3)
    test(sln, 3, 2)
    test(sln, 2, 2)
    test(sln, 1, 2)
    test(sln, 3, 1)