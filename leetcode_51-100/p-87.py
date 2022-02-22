class Solution:
    memo: map = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        Solution.memo.clear()
        return self._isScramble(s1, s2)

    def _isScramble(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if length == 1:
            return s1 == s2

        memoKey = s1 + "_" + s2
        result = Solution.memo.get(memoKey)
        if result != None:
            return result

        result = False
        for split in range(1, length):
            s1Left, s1Right = s1[:split], s1[split:]
            s2Left, s2Right = s2[:split], s2[split:]

            if self._possibleScamble(s1Left, s2Left) and self._possibleScamble(s1Right, s2Right):
                if self._isScramble(s1Left, s2Left) and self._isScramble(s1Right, s2Right):
                    result = True
                    break

            s1Left, s1Right = s1[:split], s1[split:]
            s2Left, s2Right = s2[:(length - split)], s2[(length - split):]

            if self._possibleScamble(s1Left, s2Right) and self._possibleScamble(s1Right, s2Left):
                if self._isScramble(s1Left, s2Right) and self._isScramble(s1Right, s2Left):
                    result = True
                    break
        
        Solution.memo[memoKey] = result
        return result

    def _possibleScamble(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)

def test(sln, s1, s2):
    result = sln.isScramble(s1, s2)
    print(result)
    print(len(Solution.memo))

if __name__ == "__main__":
    sln = Solution()
    test(sln, "great", "rgeat")
    test(sln, "abcde", "caebd")
    test(sln, "a", "a")
    test(sln, "abb", "bba")
    test(sln, "eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd")