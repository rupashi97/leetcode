class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        track = collections.defaultdict(int)
        
        for i in arr: track[i]+=1
            
        occ = set()
        
        for k in track:
            if track[k] in occ:
                return False
            occ.add(track[k])
            
        return True
                      