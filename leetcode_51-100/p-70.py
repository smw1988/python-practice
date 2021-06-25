memo = [0] * 46

def calcFib():
    memo[0] = 1
    memo[1] = 1
    for i in range(2, 46):
        memo[i] = memo[i - 1] + memo[i - 2]

calcFib()

class Solution:
    def climbStairs(self, n: int) -> int:
        return memo[n]

def test(sln, n):
    result = sln.climbStairs(n)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    for i in range(1, 46):
        test(sln, i)