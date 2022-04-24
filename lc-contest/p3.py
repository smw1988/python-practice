# problem: https://leetcode-cn.com/problems/ZbAuEH/submissions/
# solution:
#     dynamic programming
#     m(t[i], x, y) is the maximum possible score at position[x][y] at time t[i]
#     m(t[i], x, y) = p(t[i], x, y) + h(t[i], x, y)
#     p(t[i], x, y) = max{ m(t[i - 1], x', y') }
#                     for all (x', y') from which (x, y) is reachable within time (t[i] - t[i - 1])
#                     if (t[i] - t[i - 1]) < 4
#     p(t[i], x, y) = max{ m(t[i - 1], x', y') }
#                     for all 9 possible (x', y') positions
#                     if (t[i] - t[i - 1]) >= 4
#     h(t[i], x, y) = 1 if [t[i], x, y] exists in moles and p(t[i], x, y) >= 0
#                     0 otherwise
#
#     Categorizing p(t[i], x, y) into 2 scenarios based on time diff is not necessary for correctness
#     but critical for performance.

from typing import List
import time

class Solution:
    def getMaximumNumber(self, moles: List[List[int]]) -> int:
        timeInstants: List[int] = self._extractTimeList(moles)
        appearanceMap: dict[int, list] = self._buildAppearanceMap(moles)

        coordinates = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        currentPlan = [[-1, -1, -1], [-1, 0, -1], [-1, -1, -1]]
        nextPlan = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        start = time.time()

        lastInstant = 0
        for instant in timeInstants:
            appearances = appearanceMap[instant]
            timeDiff = instant - lastInstant

            if timeDiff >= 4:
                maxNumber = max([max(n) for n in currentPlan])
                for x in range(3):
                    for y in range(3):
                        nextPlan[x][y] = maxNumber
            else:
                for position in coordinates:
                    maxNumber = self._reachableMaximumNumber(currentPlan, position, timeDiff)
                    nextPlan[position[0]][position[1]] = maxNumber
            
            for position in appearances:
                if nextPlan[position[0]][position[1]] >= 0:
                    nextPlan[position[0]][position[1]] += 1

            # print(nextPlan)

            currentPlan = nextPlan
            nextPlan = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            lastInstant = instant

        end = time.time()
        print(end - start)

        return max([max(n) for n in currentPlan])

    def _extractTimeList(self, moles: List[List[int]]):
        instants = [m[0] for m in moles]
        instants = list(set(instants))
        instants.sort()
        return instants

    def _buildAppearanceMap(self, moles: List[List[int]]):
        appearanceMap: dict[int, list] = {}
        for mole in moles:
            time = mole[0]
            if time not in appearanceMap:
                appearanceMap[time] = []
            appearanceMap[time].append((mole[1], mole[2]))

        return appearanceMap

    def _reachableMaximumNumber(self, m: List[List[int]], pos: tuple, timeDiff: int):
        maxNumber = -1
        for x in range(3):
            for y in range(3):
                if m[x][y] >= 0 and (abs(x - pos[0]) + abs(y - pos[1])) <= timeDiff:
                    maxNumber = max(maxNumber, m[x][y])
        return maxNumber
        
def test(sln, moles: List[List[int]]):
    result = sln.getMaximumNumber(moles)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    # test(sln, [[1,1,0],[2,0,1],[4,2,2]])
    # test(sln, [[2,0,2],[5,2,0],[4,1,0],[1,2,1],[3,0,2]])
    # test(sln, [[0,1,0],[0,0,1]])