from typing import Dict

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        if self._areContentsEqual(s1, s2, s3) == False:
            return False

        # the cache is designed to hold only latest result for index2
        # calculating cache key for (2, 2) would overwrite existing cache key (1, 2)
        # this ensures space complexity has upperbound O(s2 length)
        # however, I don't understand why this still has good performance, 
        # i.e. why a full cache is not needed.
        # (actual experiment shows cache hit rate is quite high)
        memo = {}
        result = self._isInterleave(s1, s2, s3, 0, 0, 0, memo)

        #print(memo)

        return result

    def _areContentsEqual(self, s1: str, s2: str, s3: str):
        dict1 = {}; dict2 = {}
        self._collectCharCount(s1, dict1)
        self._collectCharCount(s2, dict1)
        self._collectCharCount(s3, dict2)
        return dict1 == dict2

    def _collectCharCount(self, s: str, d: dict):
        for char in s:
            count = d.get(char)
            count = 1 if count == None else count + 1
            d[char] = count

    # recursively find position in s3 for each char of s2
    def _isInterleave(self, s1: str, s2: str, s3: str, s1Index: int, s2Index: int, s3Index: int, memo: dict):
        if s2Index == len(s2):
            return s1[s1Index:] == s3[s3Index:]

        while s1Index < len(s1):
            c1 = s1[s1Index]; c2 = s2[s2Index]; c3 = s3[s3Index]

            if c1 != c3 and c2 != c3:
                return False
            
            if c1 == c3 and c2 != c3:
                s1Index += 1; s3Index += 1
                continue

            # when reaches here, c2 == c3, a match for c2 is found
            if c1 != c3:
                recResult = self._getFromMemo(s1Index, s2Index + 1, memo)
                if recResult == None:
                    recResult = self._isInterleave(s1, s2, s3, s1Index, s2Index + 1, s3Index + 1, memo)
                self._updateMemo(s1Index, s2Index + 1, recResult, memo)
                return recResult
            
            # last case: c1 == c2 == c3
            # try using c2 (so recursion) first, then try using as c1 (continue loop)
            recResult = self._getFromMemo(s1Index, s2Index + 1, memo)
            if recResult == None:
                recResult = self._isInterleave(s1, s2, s3, s1Index, s2Index + 1, s3Index + 1, memo)
            self._updateMemo(s1Index, s2Index + 1, recResult, memo)

            if recResult:
                return True

            s1Index += 1; s3Index += 1

        return s2[s2Index:] == s3[s3Index:]

    def _getFromMemo(self, i1, i2, memo):
        v = memo.get(i1)
        if v != None:
            if v[0] == i2:
                print("cache hit")
                return v[1]
            else:
                print("cache overwritten")
        else:
            return None

    def _updateMemo(self, i1, i2, v, memo):
        memo[i1] = (i2, v)

def test(sln, s1, s2, s3):
    result = sln.isInterleave(s1, s2, s3)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")
    test(sln, s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc")
    test(sln, s1 = "", s2 = "", s3 = "")
    test(sln, "abc", "abc", "aabbcd")
    test(sln, "a", "b", "ab")
    test(sln, "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", 
        "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", 
        "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")
