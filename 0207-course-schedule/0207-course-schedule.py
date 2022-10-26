import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
            
        def isCyclic(graph, visited, src, localVisited):

            if src in visited: 
                return False
            
            if src in localVisited: return True
            
            localVisited.add(src)
            
            ret = False
            for neighbor in graph[src]:
                ret = isCyclic(graph, visited, neighbor, localVisited)
                if ret: break
            
            localVisited.remove(src)
            visited.add(src)
            
            return ret
        
        
        
        graph = collections.defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        localVisited = set()
        for i in range(numCourses):
            if isCyclic(graph, visited, i, localVisited ):
                return False
        return True
        