# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, str) -> TreeNode:
        if not str:
            return None
       
        index = 0
        while index < len(str) and str[index] != "(":
            index += 1

        if not str[:index]:
            return None

        node = TreeNode(int(str[:index]))
        opens = []
        startIndex = index
        while index < len(str):
            if str[index] == "(":
                opens.append("(")
            elif str[index] == ")":
                opens.pop()
                if not opens:
                    break
            index += 1
        endIndex = index
        node.left = self.str2tree(str[startIndex + 1: endIndex])
        node.right = self.str2tree(str[endIndex + 2:-1])
        return node
