class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if len(t) == 1:
            return t if s.find(t) >= 0 else ""

        patterns = self.analyzePattern(t)


def test(sln, s, t):
    result = sln.minWindow(s, t)
    print(result)

if __name__ == "__main__":
    sln = Solution()