from typing import List

class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        total = 0
        for t in fruits:
            total += self._getTime(time, t, limit)
        return total

    def _getTime(self, time: List[int], t: List[int], limit: int):
        fruitType = t[0]
        fruitNumber = t[1]
        fruitTime = time[fruitType]
        turn = fruitNumber // limit
        if fruitNumber % limit > 0:
            turn += 1
        return fruitTime * turn

def test(sln, time, fruits, limit):
    result = sln.getMinimumTime(time, fruits, limit)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [2,3,2], [[0,2],[1,4],[2,1]], 3)
    test(sln, [1], [[0,3],[0,5]], 2)
    test(sln, [1], [[0, 3]], 3)

