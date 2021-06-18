# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.calculate(candidates, target, result, 0, [])
        return result

    def calculate(self, candidates: List[int], target: int, result: list, depth: int, temp: list):
        if (target == 0):
            result.append(temp.copy())
            return

        if (depth == len(candidates)):
            return

        use = candidates[depth]
        x = -1
        newTarget = target
        while newTarget >= 0:
            x += 1
            if (x > 0):
                temp.append(use)

            self.calculate(candidates, newTarget, result, depth + 1, temp)
            newTarget -= use

        while x > 0:
            temp.pop()
            x -= 1

        return None

def test(sln, candidates, target):
    result = sln.combinationSum(candidates, target)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [2,3,6,7], 7)
    test(sln, [2,3,5], 8)
    test(sln, [2], 1)
    test(sln, [1], 2)
    test(sln, [1], 1)