class Solution:
    
    def encode(self, strs: List[str]) -> str:
        
        return "".join([ f"{len(s)}${s}" for s in strs])
        


    def decode(self, s: str) -> List[str]:
        res=[]
        while s:
            i = s.index("$")
            v = int(s[0:i])
            res.append(s[i+1:i+1+v])
            s=s[i+v+1:]
        
        return res