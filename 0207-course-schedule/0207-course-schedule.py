import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
            
        def dfs(graph, visited, src, localVisited):

            if src in visited:    
                return True      # already visited
            
            if src in localVisited: return False  # loop detected - course cannot be completed
            
            localVisited.add(src)
            
            for neighbor in graph[src]:
                if not dfs(graph, visited, neighbor, localVisited):
                    return False
                
            localVisited.remove(src)
            visited.add(src)
            
            return True
        
        
        graph = collections.defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        localVisited = set()
        for i in range(numCourses):
            if not dfs(graph, visited, i, localVisited ):
                return False
        return True
        