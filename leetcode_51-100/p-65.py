# A valid number can be split up into these components (in order):

# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# One or more digits, followed by a dot '.'.
# One or more digits, followed by a dot '.', followed by one or more digits.
# A dot '.', followed by one or more digits.
# An integer can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One or more digits.
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

# Given a string s, return true if s is a valid number.

class Solution:
    def isNumber(self, s: str) -> bool:
        if s == "": return False

        expIndex = max(s.find("e"), s.find("E"))
        if expIndex < 0:
            return self.isDecimal(s) or self.isInteger(s)
        else:
            fractional = s[0:expIndex]
            exponent = s[expIndex + 1:]
            return (self.isDecimal(fractional) or self.isInteger(fractional)) and self.isInteger(exponent)

    def isDecimal(self, s: str):
        if s == "": return False
        if s[0] == "+" or s[0] == "-":
            s = s[1:]

        dotIndex = s.find(".")
        if dotIndex < 0: return False

        integral = s[0:dotIndex]
        fractional = s[dotIndex + 1:]
        if integral == "":
            return self.isMultipleDigits(fractional)
        elif fractional == "":
            return self.isMultipleDigits(integral)
        else:
            return self.isMultipleDigits(fractional) and self.isMultipleDigits(integral)

    def isInteger(self, s: str):
        if s == "": return False
        if s[0] == "+" or s[0] == "-":
            s = s[1:]
        return self.isMultipleDigits(s)

    def isMultipleDigits(self, s: str):
        return s.isdigit()
        

def test(sln, slist):
    for s in slist:
        result = sln.isNumber(s)
        print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"])
    test(sln, ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"])
    test(sln, ["0", "e", ".", "-1"])