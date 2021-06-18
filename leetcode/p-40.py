from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidateInfo = self.countCandidate(candidates)
        result = []
        self.calculate(candidateInfo, target, result, 0, [])
        return result

    def countCandidate(self, candidates: List[int]):
        count = {}
        for c in candidates:
            if (c in count):
                count[c] += 1
            else:
                count[c] = 1
        
        return [(n, count[n]) for n in sorted(count)]

    def calculate(self, candidates, target: int, result: list, depth: int, temp: list):
        if (target == 0):
            result.append(temp.copy())
            return

        if (depth == len(candidates)):
            return

        candidate = candidates[depth]
        use = candidate[0]
        limit = candidate[1]

        x = -1
        newTarget = target
        while newTarget >= 0 and x < limit:
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
    result = sln.combinationSum2(candidates, target)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [10,1,2,7,6,1,5], 8)
    test(sln, [2,5,2,1,2], 5)