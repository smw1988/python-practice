class BigInt:
    C = 1000000000

    def __init__(self, num: str) -> None:
        self.digits = []
        for i in range(len(num), 0, -9):
            digit = num[max(0, i - 9), i]
            self.digits.append(int(digit))

    def __init__(self, digits: list, dummy) -> None:
        self.digits = digits
    
    def add(self, other):
        digits1 =  self.digits
        digits2 = other.digits

        newDigits = []
        index1 = 0
        index2 = 0
        carry = 0

        while (index1 < len(digits1) and index2 < len(digits2)):
            (sum, carry) = self._add(digits1[index1], digits2[index2], carry)
            newDigits.append(sum)
            index1 += 1
            index2 += 1
        
        while (index1 < len(digits1)):
            (sum, carry) = self._add(digits1[index1], 0, carry)
            newDigits.append(sum)
            index1 += 1

        while (index2 < len(digits2)):
            (sum, carry) = self._add(digits2[index2], 0, carry)
            newDigits.append(sum)
            index2 += 1

        if (carry == 1):
            newDigits.append(1)

        return BigInt(newDigits, 0)

    def _add(self, d1, d2, c):
        sum = d1 + d2 + c
        if (sum >= BigInt.C):
            sum = sum - BigInt.C
            c = 1
        return (sum, c)

    def __str__(self) -> str:
        return "".join(self.digits.reverse())

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return None

def test(sln, num1: str, num2: str):
    result = sln.multiply(num1, num2)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    print(BigInt("123").add(BigInt("456")))
    #test(sln, "123", "456")