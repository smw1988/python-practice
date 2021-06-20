from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [None] * n
        for i in range(0, n):
            board[i] = ["."] * n
        self.solve(board, n, result, 0)
        return result

    def solve(self, board: List[List[str]], n: int, result: List[List[str]], depth: int):
        if depth == n:
            boardCopy = ["".join(row) for row in board]
            result.append(boardCopy)
            return

        for j in range(0, n):
            board[depth][j] = "Q"
            if self.isValid(board, n, depth, j):
                self.solve(board, n, result, depth + 1)
            board[depth][j] = "."

    def isValid(self, board: List[List[str]], n: int, depth: int, j: int):
        for i in range(0, depth):
            if board[i][j] == "Q":
                return False

        r = depth - 1
        c = j - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        r = depth - 1
        c = j + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True

def test(sln, n):
    result = sln.solveNQueens(n)
    print(result)
    print(len(result))

if __name__ == "__main__":
    sln = Solution()
    test(sln, 8)