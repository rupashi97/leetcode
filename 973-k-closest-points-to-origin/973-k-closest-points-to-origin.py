class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = collections.defaultdict(list)
        res, count = [], 0
        
        for i, [x,y] in enumerate(points):
            d = x**2 + y**2 
            dist[d].append([x,y])
            
        dsorted = sorted(list(dist.keys()))

        for d in dsorted:
            for n in range(len(dist[d])):
                res.append(dist[d][n])
                count+=1
                
            if count==k: break
            
        return res
            