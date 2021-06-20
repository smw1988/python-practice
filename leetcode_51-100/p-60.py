class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return "1"

        k = k - 1
        m = self.factorial(n)
        result = [str(i) for i in range(1, n + 1)]

        for i in range(0, n - 1):
            m = m // (n - i)
            q = k // m
            if q != 0:
                self.rotate(result, i, q)
            
            k = k % m
            if k == 0:
                break

        return "".join(result)

    def factorial(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def rotate(self, elements: list, s: int, q: int):
        t = elements[s + q]
        for i in range(q + s, s, -1):
            elements[i] = elements[i - 1]
        elements[s] = t

def test(sln, n, k):
    result = sln.getPermutation(n, k)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, 3, 3)
    test(sln, 4, 9)
    test(sln, 3, 1)
    test(sln, 2, 2)
    test(sln, 5, 120)