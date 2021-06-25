class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (len(a) < len(b)):
            t = a; a = b; b = t

        aLen = len(a)
        bLen = len(b)
        diff = aLen - bLen
        carry = 0
        result = []

        for i in range(bLen - 1, -1, -1):
            sum = int(a[i + diff]) + int(b[i]) + carry
            if sum >= 2:
                result.append(str(sum - 2))
                carry = 1
            else:
                result.append(str(sum))
                carry = 0

        for i in range(diff - 1, -1, -1):
            sum = int(a[i]) + carry
            if sum >= 2:
                result.append(str(sum - 2))
                carry = 1
            else:
                result.append(str(sum))
                carry = 0

        if carry == 1:
            result.append("1")

        result.reverse()
        return "".join(result)

def test(sln, a, b):
    result = sln.addBinary(a, b)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, "11", "1")
    test(sln, "1010", "1011")
    test(sln, "11", "0")
    test(sln, "0", "1")
    test(sln, "0", "0")
    test(sln, "1", "111")