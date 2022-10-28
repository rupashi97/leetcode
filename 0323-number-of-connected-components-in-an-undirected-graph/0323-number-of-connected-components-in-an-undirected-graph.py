import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for p in edges:
            a, b = p[0], p[1]
            graph[a].append(b)
            graph[b].append(a)
            
        visited = set()
        count = 0
        
        def dfs(src):
            
            if src in visited: return False
            visited.add(src)
            
            for neighbor in graph[src]:
                dfs(neighbor)
            
            return True
            
        
        for num in range(n):
            if dfs(num):
                count += 1
            
            
        return count
            
     