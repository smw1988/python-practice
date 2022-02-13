class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if len(t) == 1:
            return t if s.find(t) >= 0 else ""

        charPos = self.analyzeCharPos(s)
        patterns = self.analyzePattern(t)

        ranges = set()
        for (char, count) in patterns:
            indexRanges = self.generateIndexRanges(char, count, charPos)

            tempRanges = set()
            for indexRange in indexRanges:
                for oldIndexRange in ranges:
                    newRange = self.combineRange(oldIndexRange, indexRange)
                    self.mergeRanges(tempRanges, newRange)

            ranges = tempRanges

        minRange = min(ranges, key=lambda r: r[1] - r[0] + 1)
        return s[minRange[0], minRange[1] + 1]

def test(sln, s, t):
    result = sln.minWindow(s, t)
    print(result)

if __name__ == "__main__":
    sln = Solution()