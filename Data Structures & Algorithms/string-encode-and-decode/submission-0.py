class Solution:
    
    def encode(self, strs: List[str]) -> str:
        
        return "".join([ f"{len(s)}${s}" for s in strs])
        


    def decode(self, s: str) -> List[str]:
        res=[]
        while s:
            print(s)
            i = s.index("$")
            print(i)
            v = int(s[0:i])
            print(i, v, s[i+1:i+1+v])
            res.append(s[i+1:i+1+v])
            print("last - ", s[i+v+1:])
            s=s[i+v+1:]
            print(s)
        
        return res