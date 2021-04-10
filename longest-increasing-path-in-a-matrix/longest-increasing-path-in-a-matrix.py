from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def longest(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            best = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and matrix[x][y] < matrix[nx][ny]:
                    best = max(best, longest(nx, ny) + 1)

            memo[(x, y)] = best
            return best

        best = 0
        for sx in range(rows):
            for sy in range(cols):
                best = max(best, longest(sx, sy) + 1)

        return best
