class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (c == "(" or c == "[" or c == "{"):
                stack.append(c)
            elif (len(stack) == 0):
                return False
            else:
                top = stack.pop()
                if (top != "(" and c == ")"):
                    return False
                if (top != "[" and c == "]"):
                    return False
                if (top != "{" and c == "}"):
                    return False
        return False
