class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        if (num >= 1000):
            s = s + self.processMillenium(num // 1000)
            num = num % 1000
        if (num >= 100):
            s = s + self.processCentury(num // 100)
            num = num % 100
        if (num >= 10):
            s = s + self.processTens(num // 10)
            num = num % 10
        if (num >= 1):
            s = s + self.processDigit(num)
        return s

    def processMillenium(self, num):
        return "M" * num
    
    def processCentury(self, num):
        if (num == 9): return "CM"
        if (num == 4): return "CD"
        s = ""
        if (num >= 5):
            s = "D"
            num = num - 5
        s = s + num * "C"
        return s
    
    def processTens(self, num):
        if (num == 9): return "XC"
        if (num == 4): return "XL"
        s = ""
        if (num >= 5):
            s = "L"
            num = num - 5
        s = s + num * "X"
        return s
    
    def processDigit(self, num):
        if (num == 9): return "IX"
        if (num == 4): return "IV"
        s = ""
        if (num >= 5):
            s = "V"
            num = num - 5
        s = s + num * "I"
        return s

if __name__ == '__main__':
    s = Solution()
    text = s.intToRoman(1994)
    print(text)