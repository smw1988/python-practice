from typing import List
from functools import reduce

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        temp = [None] * (n * 2)
        self.generate(result, n, 0, 0, temp, 0)
        return result

    def generate(self, result: List[str], n: int, open: int, closed: int, temp: List[str], index: int):
        if (closed == n):
            final = reduce(lambda s1, s2: s1 + s2, temp)
            result.append(final)
            return
        
        if (open + closed < n):
            temp[index] = "("
            self.generate(result, n, open + 1, closed, temp, index + 1)
        if (open > 0):
            temp[index] = ")"
            self.generate(result, n, open - 1, closed + 1, temp, index + 1)


if __name__ == "__main__":
    s = Solution()
    result = s.generateParenthesis(1)
    print(result)