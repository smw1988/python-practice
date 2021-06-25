from math import floor
from math import sqrt

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x < 4: return 1
        guess = 1
        while True:
            q = x / guess
            newGuess = (guess + q) / 2

            if floor(guess) == floor(newGuess):
                return floor(guess)

            guess = newGuess

            # if abs(guess - newGuess) < 1:
            #     return floor(max(guess, newGuess))

def test(sln, x):
    result = sln.mySqrt(x)
    print(x, result, sqrt(x), sep = ", ")

if __name__ == "__main__":
    sln = Solution()
    for i in range(1, 100):
        test(sln, i)
    