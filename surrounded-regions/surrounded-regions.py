class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(matrix, x, y):
            
            queue = [(x, y)]
            sides = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited = {}
            while queue:
                sz = len(queue)
                is_valid = True
                while sz:
                    x, y = queue.pop()
                    visited[(x, y)] = True
                    matrix[x][y] = 'X'
                    for dx, dy in sides:
                        if (x + dx == 0 or x + dx == len(matrix) - 1 or\
                           y + dy == 0 or y + dy == len(matrix[0]) - 1) and \
                            matrix[x + dx][y + dy] == 'O':
                            is_valid = False
                            break
                        
                        if matrix[x + dx][y + dy] == 'O':
                            queue.append((x + dx, y + dy))
                    if not is_valid:
                        break
                    sz -= 1
                if not is_valid:
                    break
            
            if not is_valid:
                for k, v in visited.items():
                    x, y = k
                    matrix[x][y] = 'O'
        
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == 'O':
                    bfs(board, i, j)
        