class Solution:
    def valSquare(self, board: List[List[str]], x, y) -> bool:
        valSet=set()
        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in valSet:
                        return False
                    valSet.add(board[i][j])
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col=len(board), len(board[0])
        out=True
        for i in range(0, row, 3):
            for j in range(0, col, 3):
                out = out and self.valSquare(board, i, j)
        
        for i in range(0, row):
            colSet=set()
            for j in range(0, col):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in colSet:
                        return False
                    colSet.add(board[i][j])
        for j in range(0, col):
            rowSet=set()
            for i in range(0, row):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in rowSet:
                        return False
                    rowSet.add(board[i][j])
        
        return out