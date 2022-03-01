from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count = len(prices)
        if count == 1:
            return 0

        if count == 2:
            profit = prices[1] - prices[0]
            return profit if profit > 0 else 0
        
        t = prices
        count -= 1
        for i in range(count):
            t[i] = t[i + 1] - t[i]
        t[count] = None

        #print(t)

        a1 = [t[0]] * count # a1[i] is max profit for ops in p[0] to [i]
        a2 = [t[count - 1]] * count # a2[i] is max profit for ops in p[i] to p[count - 1]
        
        for i in range(1, count):
            a1[i] = a1[i - 1] + t[i] if a1[i - 1] > 0 else t[i]
        #print(a1)
        for i in range(1, count):
            a1[i] = max(a1[i - 1], a1[i])
        #print(a1)

        for i in range(count - 2, -1, -1):
            a2[i] = a2[i + 1] + t[i] if a2[i + 1] > 0 else t[i]
        #print(a2)
        for i in range(count - 2, -1, -1):
            a2[i] = max(a2[i + 1], a2[i])
        #print(a2)
                
        m = max(0, a1[count - 1])
        for i in range(count - 1):
            profit = a1[i] + a2[i + 1]
            if profit > m:
                m = profit
                
        return m

def test(sln, prices):
    result = sln.maxProfit(prices)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [3,3,5,0,0,3,1,4])
    test(sln, [1,2,3,4,5])
    test(sln, [7,6,4,3,1])
    test(sln, [1,2,4,2,5,7,2,4,9,0])