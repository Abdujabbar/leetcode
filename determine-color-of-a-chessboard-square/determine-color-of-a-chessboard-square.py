class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        board = []
        
        isWhite = True
        
        for i in range(8):
            row = []
            for j in range(8):
                if not row:
                    row.append(isWhite)
                else:
                    row.append(not row[-1])
            board.append(row)
            isWhite = not isWhite
        x, y = ord(coordinates[0]) - ord('a') - 1, int(coordinates[1]) - 1
        
        return board[x][y]