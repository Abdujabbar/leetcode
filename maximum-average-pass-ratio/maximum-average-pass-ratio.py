import heapq

        
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def profit(a, b):
            return (a + 1) / (b + 1) - a / b
        
        
        maxHeap = []
        for passed, total in classes:
            maxHeap.append((-profit(passed * 1.0, total * 1.0), passed * 1.0, total * 1.0))
     
        heapq.heapify(maxHeap)
        while extraStudents:
            d, a, b = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-profit(a + 1, b + 1), a + 1, b + 1))
            extraStudents -= 1
        
        total = 0
        for d, a, b in maxHeap:
            total += a / b
        return total / len(classes)