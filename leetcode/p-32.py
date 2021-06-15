class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if (len(s) <= 1):
            return 0
        
        stack = []
        open = 0
        longest = 0

        for c in s:
            if (c == "("):
                stack.append(-1)
                open += 1
            else:
                if (open > 0):
                    self.reduce(stack)
                    open -= 1
                elif (len(stack) > 0):
                    candidate = stack[0]
                    longest = max(longest, candidate)
                    stack.clear()

        longest = max(longest, max(stack, default=0))

        return longest

    def reduce(self, stack: list):
        matched = False
        length = 0

        for i in range(len(stack) - 1, -1, -1):
            e = stack[i]
            if (e == -1 and matched):
                break
            
            stack.pop()
            if (e == -1):
                length += 2
                matched = True
            else:
                length += e
        
        stack.append(length)


def test(sln, s):
    result = sln.longestValidParentheses(s)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "(()")
    test(sln, ")()())")
    test(sln, "()(()")
    test(sln, "))))())()()(()")