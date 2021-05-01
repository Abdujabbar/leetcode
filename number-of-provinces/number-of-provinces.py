from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(isConnected)):
            childs = isConnected[i]
            for j in range(len(childs)):
                if childs[j] == 1:
                    graph[i].append(j)
        
        n = len(isConnected[0])
        
        def travel(node):
            
            visited[node] = True
            
            for n in graph[node]:
                if not visited[n]:
                    travel(n)
        
        visited = defaultdict(int)
        counter = 0
        
        for node in range(n):
            if not visited[node]:
                counter += 1
                travel(node)
        
        return counter