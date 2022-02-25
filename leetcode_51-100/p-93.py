from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        current = [None] * 4
        self._restoreIpAddresses(s, 0, 4, result, current)
        return result

    def _restoreIpAddresses(self, s: str, startIndex: int, remain: int, result: list, current: List[str]):
        if remain == 0:
            if startIndex == len(s):
                result.append(".".join(current))
            return

        if startIndex >= len(s):
            return

        current[4 - remain] = s[startIndex]
        self._restoreIpAddresses(s, startIndex + 1, remain - 1, result, current)

        if s[startIndex] == "0":
            return

        if startIndex + 1 < len(s):
            current[4 - remain] = s[startIndex:startIndex + 2]
            self._restoreIpAddresses(s, startIndex + 2, remain - 1, result, current)
        
        if startIndex + 2 < len(s):
            number = int(s[startIndex:startIndex + 3])
            if number < 256:
                current[4 - remain] = s[startIndex:startIndex + 3]
                self._restoreIpAddresses(s, startIndex + 3, remain - 1, result, current)

def test(sln, s):
    result = sln.restoreIpAddresses(s)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "25525511135")
    test(sln, "101023")
    test(sln, "0000")
    test(sln, "00002")
    test(sln, "00000")