# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]

# s = "wordgoodgoodgoodbestword" words = ["word","good","best","good"]
# Output: [8]

from typing import List
from collections import deque

class StrAux:
    def strStr(s: str, p: str) -> list:
        if (len(p) == 0):
            return [0]

        if (len(s) == 0):
            return []

        if (s == p):
            return [0]

        if (len(s) < len(p)):
            return []

        i = 0
        j = 0
        aux = StrAux.calculateLongestProperPrefixSuffix(p)

        #print(aux)
        result = []

        while (i < len(s)):
            if (s[i] == p[j]):
                i += 1
                j += 1
                if (j == len(p)):
                    result.append(i - j)
                    j = aux[j - 1]
            elif (j == 0):
                i += 1
            else:
                j = aux[j - 1]

        return result

    def calculateLongestProperPrefixSuffix(p: str):
        aux = [None] * len(p)

        aux[0] = 0
        for i in range(1, len(p)):
            k = i
            while (k > 0):
                k = aux[k - 1]
                if (p[k] == p[i]):
                    aux[i] = k + 1
                    break
            
            if (aux[i] == None):
                aux[i] = 0

        return aux

class Solution:
    def removeDup(self, words: List[str]):
        m = {}
        for w in words:
            if (w in m):
                m[w] = m[w] + 1
            else:
                m[w] = 1
        
        count = len(m)
        newWords = [None] * count
        wordLimit = [None] * count

        i = 0
        for w in m.keys():
            newWords[i] = w
            wordLimit[i] = m[w]
            i += 1

        return (newWords, wordLimit)

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        fullWordCount = len(words)
        (words, wordLimit) = self.removeDup(words)

        wordLen = len(words[0])
        wordsCount = len(words)
        strLen = len(s)
        result = []

        memo = [None] * strLen
        for i in range(0, wordsCount):
            w = words[i]
            occurrences = StrAux.strStr(s, w)
            for o in occurrences:
                memo[o] = i
        
        q = deque()

        for start in range(0, wordLen):
            membership = [0] * wordsCount
            memberCount = 0
            q.clear()

            for i in range(start, strLen, wordLen):
                wordIndex = memo[i]
                if (wordIndex != None):
                    if (membership[wordIndex] < wordLimit[wordIndex]):
                        membership[wordIndex] += 1
                        memberCount += 1
                        q.append(i)
                        
                        if (memberCount == fullWordCount):
                            strIndex = q.popleft()
                            memberCount -= 1
                            result.append(strIndex)
                            firstWordIndex = memo[strIndex]
                            membership[firstWordIndex] -= 1
                    else:
                        firstWordIndex = None
                        while (firstWordIndex != wordIndex):
                            strIndex = q.popleft()
                            memberCount -= 1
                            firstWordIndex = memo[strIndex]
                            membership[firstWordIndex] -= 1
                        
                        membership[wordIndex] += 1
                        memberCount += 1
                        q.append(i)
                else:
                    membership = [0] * wordsCount
                    memberCount = 0
                    q.clear()

        return result

def test(sln, s, words):
    result = sln.findSubstring(s, words)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "barfoothefoobarman", ["foo","bar"])
    test(sln, "wordgoodgoodgoodbestword", ["word","good","best","word"])
    test(sln, "barfoofoobarthefoobarman", ["bar","foo","the"])
    test(sln, "wordgoodgoodgoodbestword", ["word","good","best","good"])
    test(sln, "aaaa", ["aa","aa"])