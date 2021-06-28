class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        best = 0
        left = 0
        counter = 0
        for right in range(len(arr)):

            if arr[right] == 0:
                counter += 1

            while (right - left + 1 - (right - left + 1 - counter)) > k:
                if arr[left] == 0:
                    counter -= 1
                left += 1

            best = max(best, right - left + 1)

        return best