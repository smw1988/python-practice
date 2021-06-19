class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if (p == ""):
            return s == ""

        lastStar = p.rfind("*")
        lastQuestionMark = p.rfind("?")
        if lastStar >= 0 and lastStar > lastQuestionMark:
            endPattern = p[lastStar + 1:]
            if (endPattern != "" and not s.endswith(endPattern)):
                return False

        memo = {}
        p = self.removeDuplicateStar(p)
        return self.match(s + "$", p + "$", 0, 0, memo)

    def removeDuplicateStar(self, p: str):
        p2 = ""
        hitStar = False

        for c in p:
            if (c == "*"):
                if (hitStar != True):
                    p2 += c
                    hitStar = True
            else:
                p2 += c
                hitStar = False
        
        return p2

    def match(self, s: str, p: str, i: int, j: int, memo):
        if (i == len(s) and j == len(p)):
            return True

        if (i == len(s) or j == len(p)):
            return False

        if (i, j) in memo:
            return memo[(i, j)]

        result = None
        if (p[j] == "*"):
            result = self.match(s, p, i, j + 1, memo) or self.match(s, p, i + 1, j, memo) or self.match(s, p, i + 1, j + 1, memo)
        else:
            result = (p[j] == "?" or s[i] == p[j]) and self.match(s, p, i + 1, j + 1, memo)

        memo[(i, j)] = result
        return result

def test(sln, s: str, p: str):
    result = sln.isMatch(s, p)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "aa", "a")
    test(sln, "aa", "*")
    test(sln, "cb", "?a")
    test(sln, "adceb", "*a*b")
    test(sln, "acdcb", "a*c?b")
    test(sln, "", "******")
    test(sln, "babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b")
    test(sln, "bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab", "b*b*ab**ba*b**b***bba")
    test(sln, "abefcdgiescdfimde", "ab*cd?i*de")
    test(sln, "hi", "*?")
    test(sln, "abcd", "*?*?*?*?")
    test(sln, "bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa", "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****")
    