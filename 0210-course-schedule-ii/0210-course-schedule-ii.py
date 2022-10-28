import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        for p in prerequisites:
            a, b = p[0], p[1]
            graph[a].append(b)
            
        stack = []
        visited, path = set(), set()
        
        def dfs(crs):
            
            if crs in visited: return True # skip visited nodes
            
            if crs in path: return False # cycle
            path.add(crs)
            
            for neighbor in graph[crs]:
                if not dfs(neighbor):
                    return False
                
            path.remove(crs)
            stack.append(crs)
            visited.add(crs)
            
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return stack    
        