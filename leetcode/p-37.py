from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        temp = self.copyBoard(board)
        result = self.solve(temp, 0, 0)
        self.copyResult(temp, board)
        return result

    def copyBoard(self, board: List[List[str]]):
        temp = [None] * 9
        for row in range(0, 9):
            originalRow = board[row]
            newRow = [None] * 9
            temp[row] = newRow

            for column in range(0, 9):
                cell = originalRow[column]
                if (cell != '.'):
                    newRow[column] = int(cell)

        return temp
    
    def solve(self, board, row, column):
        if (row == 9):
            return True

        nextColumn = 0 if column == 8 else column + 1
        nextRow = row + 1 if nextColumn == 0 else row

        if board[row][column] != None:
            return self.solve(board, nextRow, nextColumn)
        
        for candidate in range(1, 10):
            board[row][column] = candidate
            if (self.check(board, row, column)):
                if (self.solve(board, nextRow, nextColumn)):
                    return True

        board[row][column] = None
        return False

    def copyResult(self, digitBoard, strBoard):
        for row in range(0, 9):
            for column in range(0, 9):
                strBoard[row][column] = str(digitBoard[row][column])

    def check(self, board, row, column):
        if (self.checkUnit(board[row]) != True):
            return False

        if (self.checkUnit(self.generateColumn(board, column)) != True):
            return False

        box = self.generateBox(board, row - row % 3, column - column % 3)
        if (self.checkUnit(box) != True):
            return False

        return True

    def generateColumn(self, board, column: int):
        for row in range(0, 9):
            yield board[row][column]
    
    def generateBox(self, board, row, column):
        for i in range(0, 3):
            for j in range(0, 3):
                yield board[row + i][column + j]

    def checkUnit(self, cells):
        memo = [None] * 10
        for c in [c for c in cells if c != None]:
            if (memo[c] != None):
                return False
            else:
                memo[c] = 1
        return True

def test(sln, board):
    result = sln.solveSudoku(board)
    print(result)
    print(board)

if __name__ == "__main__":
    sln = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    test(sln, board)

    board = [[".",".",".",".",".","7",".",".","9"],
             [".","4",".",".","8","1","2",".","."],
             [".",".",".","9",".",".",".","1","."],
             [".",".","5","3",".",".",".","7","2"],
             ["2","9","3",".",".",".",".","5","."],
             [".",".",".",".",".","5","3",".","."],
             ["8",".",".",".","2","3",".",".","."],
             ["7",".",".",".","5",".",".","4","."],
             ["5","3","1",".","7",".",".",".","."]]
    test(sln, board)