class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= 1:
            return "0"
        
        if len(num) == 2:
            return num[0] if int(num[0]) < int(num[1]) else num[1]
        
        stack = [num[0]]
        
        for i in range(1, len(num)):
            while stack and int(stack[-1]) > int(num[i]) and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while len(stack) > 1 and stack[0] == "0":
            stack.pop(0)
        
        while stack and k > 0:
            if int(stack[-1]) > int(stack[0]):
                stack.pop()
            else:
                stack.pop(0)
            k -= 1
        
        return "".join(stack) if stack else "0"
            
        
        