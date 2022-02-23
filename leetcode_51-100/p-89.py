from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        code = [0] * n
        result = []
        result.append("".join(map(str, code)))

        self._grayCode(n, 0, code, result)
        return [int(s, 2) for s in result]

    def _grayCode(self, n: int, current: int, code: List[int], result: List[str]):
        if current == n - 1:
            code[current] = 1 - code[current]
            result.append("".join(map(str, code)))
        else:
            self._grayCode(n, current + 1, code, result)
            code[current] = 1 - code[current]
            result.append("".join(map(str, code)))
            self._grayCode(n, current + 1, code, result)

def test(sln, n):
    result = sln.grayCode(n)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, 1)
    test(sln, 2)
    test(sln, 3)
    test(sln, 4)