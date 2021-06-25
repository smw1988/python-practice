from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            sum = digits[i] + carry
            if sum >= 10:
                digits[i] = sum - 10
                carry = 1
            else:
                digits[i] = sum
                carry = 0
        
        if carry == 1:
            digits.insert(0, 1)
        
        return digits

def test(sln, digits):
    result = sln.plusOne(digits)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [1,2,3])
    test(sln, [4,3,2,1])
    test(sln, [0])
    test(sln, [9, 9, 9, 9])