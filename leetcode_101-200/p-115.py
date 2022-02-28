class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sLen = len(s)
        tLen = len(t)

        if sLen < tLen:
            return 0

        if sLen == tLen:
            return 1 if s == t else 0

        matrix = [[0] * tLen for _ in range(sLen)]

        matrix[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, sLen):
            matrix[i][0] = matrix[i - 1][0] + 1 if s[i] == t[0] else matrix[i - 1][0]

        for i in range(1, sLen):
            for j in range(1, tLen):
                if s[i] == t[j]:
                    matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j]

        return matrix[sLen - 1][tLen - 1]
                
def test(sln, s, t):
    result = sln.numDistinct(s, t)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "aaaab", "aab")
    test(sln, "rabbbit", "rabbit")
    test(sln, "babgbag", "bag")