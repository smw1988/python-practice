from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengthLimit = min(map(len, strs))
        
        lcp = ""
        index = 0
        while (index < lengthLimit):
            charset = list(set(map(lambda s: s[index], strs)))
            if (len(charset) == 1):
                lcp += charset[0]
                index += 1
            else:
                break

        return lcp


if __name__ == "__main__":
    s = Solution()
    strs = ["flower","flow","flight"]
    str = s.longestCommonPrefix(strs)
    print(str)