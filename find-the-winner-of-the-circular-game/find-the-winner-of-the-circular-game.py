class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [q for q in range(1, n + 1)]
        index = 0
        while len(arr) != 1:
            current = index + k - 1
            current %= len(arr)
            arr.pop(current)
            index = current
            
        return arr[-1]