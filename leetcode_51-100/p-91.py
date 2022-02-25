from operator import mul
from functools import reduce
from typing import List

class Solution:
    fib: List[int] = None

    def numDecodings(self, s: str) -> int:
        if Solution.fib == None:
            Solution.fib = Solution.calculateFib()

        segments = self._segment(s)
        if segments == None:
            return 0
        print(segments)
        return reduce(mul, [self._numDecodings(s) for s in segments], 1)

    def calculateFib() -> List[int]:
        f = [1] * 101
        f[1] = 1
        f[2] = 2
        for i in range(3, 101):
            f[i] = f[i - 1] + f[i - 2]
        
        return f

    def _segment(self, s: str):
        result = []
        length = len(s)
        start = 0

        while start < length:
            if s[start] == "0":
                return None

            index = start + 1; end = index
            while index < length:
                digit1 = int(s[index - 1])
                digit2 = int(s[index])

                if digit2 == 0 and digit1 > 2:
                    return None
                if digit2 == 0 and digit1 < 3:
                    end = index - 1
                    index += 1
                    break
                if 10 * digit1 + digit2 > 26:
                    break

                index += 1
                end = index

            if start != end:
                result.append(s[start:end])
            start = index

        return result

    def _numDecodings(self, s: str):
        return Solution.fib[len(s)]

def test(sln, s):
    result = sln.numDecodings(s)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "10")
    test(sln, "226")
    test(sln, "06")
    test(sln, "226116")
    test(sln, "11261203")
    test(sln, "1203")