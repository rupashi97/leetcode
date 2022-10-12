class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        track = collections.defaultdict(int)
        
        for i in arr: track[i]+=1
            
        occ = set()
        
        for k,v in track.items():
            if v in occ:
                return False
            occ.add(v)
            
        return True
                      