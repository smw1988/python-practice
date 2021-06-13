class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = haystack
        p = needle

        if (len(p) == 0):
            return 0

        if (len(s) == 0):
            return -1

        if (s == p):
            return 0

        if (len(s) < len(p)):
            return -1

        i = 0
        j = 0
        aux = self.calculateLongestProperPrefixSuffix(p)

        #print(aux)

        while (i < len(s)):
            if (s[i] == p[j]):
                i += 1
                j += 1
                if (j == len(p)):
                    return i - j
            elif (j == 0):
                i += 1
            else:
                j = aux[j - 1]

        return -1

    def calculateLongestProperPrefixSuffix(self, p: str):
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

if __name__ == "__main__":
    s = Solution()
    result = s.strStr("AAAAAAAAAAAAAAAAAB", "AAABAAA")
    print(result)