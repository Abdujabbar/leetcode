from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        maxNode = -1
        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
            maxNode = max(maxNode, max(a, b))
            
        for vertex, edges in graph.items():
            if len(edges) == maxNode - 1:
                return vertex
        
        return 0