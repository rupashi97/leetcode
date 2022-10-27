import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        for p in prerequisites:
            a, b = p[0], p[1]
            graph[a].append(b)
        
        def dfs(crs, stack, visited, path):
            
            if crs in visited: return True # skip visited nodes
            
            if crs in path: return False # cycle
            path.add(crs)
            
            for neighbor in graph[crs]:
                if not dfs(neighbor, stack, visited, path):
                    return False
                
            stack.append(crs)
            visited.add(crs)
            
            return True
            
            
        stack = []
        visited = set()
        path = set()
        for i in range(numCourses):
            if not dfs(i, stack, visited, path):
                return []
            
        return stack    
        