from typing import List
from functools import reduce

class Solution:
    letters = [ [], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], 
        ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"] ]

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        temp = [None] * len(digits)
        self.combine(digits, 0, result, temp)
        return result

    def combine(self, digits: str, depth: int, result: List[str], temp: List[str]):
        if (depth == len(digits)):
            s = reduce(lambda s1, s2: s1 + s2, temp, "")
            result.append(s)
        else:
            d = int(digits[depth])
            choices = self.letters[d]
            for c in choices:
                temp[depth] = c
                self.combine(digits, depth + 1, result, temp)

if __name__ == "__main__":
    s = Solution()
    digits = "23"
    result = s.letterCombinations(digits)
    print(result)
