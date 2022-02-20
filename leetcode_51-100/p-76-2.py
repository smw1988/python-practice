class Solution:
    letterCount = ord("z") - ord("A") + 1

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if len(t) == 1:
            return t if s.find(t) >= 0 else ""

        # t's pattern is a summary of the number of occurrence of each letter in t
        # e.g. [a:2, b:1], the key of this dictionary is translated from letter to number based on ascii 
        patterns = self.analyzePattern(t)
        patternLetterCount = sum(p > 0 for p in patterns)

        # charPos is a summary of (letter, position) of each letter in t
        # e.g. [(a,0), (b,2)], letter is tranlated from letter to number based on ascii
        charPos = self.analyzeCharPos(s, patterns)

        if len(charPos) < len(t):
            return ""

        minWindowSize = len(s) + 1
        minWindow = None

        leftEndIndex = 0 
        rightEndIndex = -1
        direction = +1 # move right cursor
        satisfiedCount = 0
        satisfactionTable = [0] * Solution.letterCount

        while True:
            if direction > 0: # move right cursor
                rightEndIndex += 1
                if rightEndIndex >= len(charPos):
                    break

                # include the impact of right end
                rightEnd = charPos[rightEndIndex]
                satisfactionTable[rightEnd[0]] += 1
                if satisfactionTable[rightEnd[0]] == patterns[rightEnd[0]]:
                    satisfiedCount += 1

            else: # move left cursor, and remove the impact of left end
                leftEnd = charPos[leftEndIndex]
                satisfactionTable[leftEnd[0]] -= 1
                if satisfactionTable[leftEnd[0]] == patterns[leftEnd[0]] - 1:
                    satisfiedCount -= 1
                leftEndIndex += 1

            if satisfiedCount == patternLetterCount:
                leftIndexInS = charPos[leftEndIndex][1]
                rightIndexInS = charPos[rightEndIndex][1]
                windowSize = rightIndexInS - leftIndexInS + 1
                if windowSize < minWindowSize:
                    minWindowSize = windowSize
                    minWindow = (leftIndexInS, rightIndexInS)
                direction = -1
            else:
                direction = +1

        if minWindow == None:
            return ""
        else:
            return s[(minWindow[0]):(minWindow[1] + 1)]

    def analyzePattern(self, t: str):
        patterns = [0] * Solution.letterCount
        for c in t:
            patterns[ord(c) - ord("A")] += 1
        return patterns

    def analyzeCharPos(self, s: str, patterns):
        charPos = []
        for (indexInS, c) in enumerate(s):
            index = ord(c) - ord("A")
            if patterns[index] > 0:
                charPos.append((index, indexInS))
        return charPos

def test(sln, s, t):
    result = sln.minWindow(s, t)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "ADOBECODEBANC", "CBBB")
    test(sln, "a", "a")
    test(sln, "a", "aa")