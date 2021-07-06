class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.routes = []
        def dfs(curr_node, path):
            if curr_node == len(graph) - 1:
                self.routes.append(path)
                return
            
            for next_node in graph[curr_node]:
                dfs(next_node, path + [next_node])
            
        
        dfs(0, [0])
        
        return self.routes
            
            