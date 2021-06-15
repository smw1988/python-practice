memo = [None] * 31
memo[1] = "1"

class Solution:
    def countAndSay(self, n: int) -> str:
        if (memo[n] != None):
            return memo[n]

        for index in range(1, n + 1):
            self.calculate(index)

        return memo[n]

    def calculate(self, n):
        if (memo[n] != None):
            return

        text = memo[n - 1]
        newText = ""

        lastChar = None
        count = 0
        for c in (text + "$"):
            if (c == lastChar):
                count += 1
            else:
                if (count > 0):
                    newText = newText + str(count) + lastChar
                lastChar = c
                count = 1
        
        memo[n] = newText
        

def test(sln, n):
    result = sln.countAndSay(n)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    for n in range(1, 30):
        test(sln, n)