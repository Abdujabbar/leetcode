class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(x) for x in boxes]
        prefix = [0]
        suffix = [0]
        total = boxes[0]
        ans = []
        
        for i in range(1, len(boxes)):
            prefix.append(total + prefix[-1])
            total += boxes[i]
        
        total = boxes[-1]
        for i in range(len(boxes) - 2, -1, -1):
            suffix.append(total + suffix[-1])
            total += boxes[i]    
        
        suffix.reverse()
        for i in range(len(prefix)):
            ans.append(prefix[i] + suffix[i])
        
        return ans