class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1); len2 = len(word2)
        m = [None] * (len1 + 1)
        for i in range(len1 + 1):
            m[i] = [None] * (len2 + 1)

        for i in range(len1):
            m[i][len2] = len1 - i
        for j in range(len2):
            m[len1][j] = len2 - j
        m[len1][len2] = 0

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    m[i][j] = m[i + 1][j + 1]
                else:
                    m[i][j] = min(m[i + 1][j + 1], m[i][j + 1], m[i + 1][j]) + 1

        return m[0][0]

def test(sln, word1, word2):
    result = sln.minDistance(word1, word2)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "horse", "ros")
    test(sln, "intention", "execution")