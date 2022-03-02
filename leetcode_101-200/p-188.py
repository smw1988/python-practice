from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0

        count = len(prices)
        if count <= 1:
            return 0

        if count == 2:
            profit = prices[1] - prices[0]
            return profit if profit > 0 else 0
        
        k += 1
        # m[n][k][a]
        # n: using first n prices
        # k: finished k actions (buy and sell)
        # a(ction): in which situation: bought/sold 
        m = [[[0, 0] for _ in range(k)] for _ in range(count)]

        # this achieves the effect that maybe less than k actions are needed
        for i in range(k):
            m[0][i][0] = -prices[0] # using only price[0] and in bought situation, must have bought price[0]
            m[0][i][1] = 0

        for i in range(1, count):
            for j in range(k):
                m[i][j][0] = max(m[i - 1][j][0], m[i - 1][j][1] - prices[i])

                # m[i][0][1] = 0 is as if the first i prices are not used
                m[i][j][1] = 0 if j == 0 else max(m[i - 1][j][1], m[i - 1][j - 1][0] + prices[i])
        
        #self._print(m, count, k)

        return m[count - 1][k - 1][1]

    def _print(self, m, n, k):
        for i in range(n):
            print(m[i])

def test(sln, k, prices):
    result = sln.maxProfit(k, prices)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, 2, [2,4,1])
    test(sln, 2, [3,2,6,5,0,3])
    test(sln, 2, [3,3,5,0,0,3,1,4])
    test(sln, 2, [1,2,3,4,5])
    test(sln, 2, [7,6,4,3,1])
    test(sln, 2, [1,2,4,2,5,7,2,4,9,0])

