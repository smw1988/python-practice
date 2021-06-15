from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if (self.check(row) != True):
                return False

        for index in range(0, 9):
            column = self.generateColumn(board, index)
            if (self.check(column) != True):
                return False

        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                box = self.generateBox(board, row, column)
                if (self.check(box) != True):
                    return False
        
        return True

    def generateColumn(self, board, column: int):
        for row in range(0, 9):
            yield board[row][column]
    
    def generateBox(self, board, row, column):
        for i in range(0, 3):
            for j in range(0, 3):
                yield board[row + i][column + j]

    def check(self, cells):
        memo = [None] * 10
        for c in [c for c in cells if c != "."]:
            v = int(c)
            if (v <= 0 or v > 9):
                return False
            if (memo[v] != None):
                return False
            else:
                memo[v] = 1
        return True
            

def test(sln, board):
    result = sln.isValidSudoku(board)
    print(result)

if __name__ == "__main__":
    sln = Solution()
    board = [[".",".",".",".","5",".",".","1","."],
             [".","4",".","3",".",".",".",".","."],
             [".",".",".",".",".","3",".",".","1"],
             ["8",".",".",".",".",".",".","2","."],
             [".",".","2",".","7",".",".",".","."],
             [".","1","5",".",".",".",".",".","."],
             [".",".",".",".",".","2",".",".","."],
             [".","2",".","9",".",".",".",".","."],
             [".",".","4",".",".",".",".",".","."]]
    test(sln, board)