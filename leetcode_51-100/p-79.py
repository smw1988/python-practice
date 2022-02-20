from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        visitingRecord = [[False] * columns for _ in range(rows)]
        return self._exist(board, word, None, 0, visitingRecord)

    def _exist(self, board: List[List[str]], word: str, startNode, startCharIndex, visitingRecord):
        if startCharIndex == len(word):
            return True

        nextNodes = self._getPossibleNextNodes(board, startNode, word[startCharIndex], visitingRecord)
        for node in nextNodes:
            visitingRecord[node[0]][node[1]] = True
            if self._exist(board, word, node, startCharIndex + 1, visitingRecord):
                return True
            visitingRecord[node[0]][node[1]] = False

        return False

    def _getPossibleNextNodes(self, board: List[List[str]], startNode, char: str, visitingRecord: List[List[bool]]):
        if startNode == None:
            return self._allNodesForChar(board, char)

        rowCount = len(board); columnCount = len(board[0])
        row = startNode[0]; column = startNode[1]
        candidates = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]

        return [n for n in candidates if 0 <= n[0] < rowCount and 0 <= n[1] < columnCount
                and visitingRecord[n[0]][n[1]] == False and board[n[0]][n[1]] == char]

    def _allNodesForChar(self, board: List[List[str]], char: str):
        rowCount = len(board); columnCount = len(board[0])
        return [(r, c) for r in range(rowCount) for c in range(columnCount) if board[r][c] == char]

def test(sln, board, word):
    result = sln.exist(board, word)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    test(sln, [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    test(sln, [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    test(sln, [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    test(sln, [["a"]], "b")