import copy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l1,l2=len(s1),len(s2)

        mp=defaultdict(int)

        for ch in s1:
            mp[ch]+=1

        i=0
        tmp=copy.deepcopy(mp)

        while(i<(l2-l1+1)):
            j=i
            temps=0
            

            
            while(temps<l1 and s2[j] in tmp and tmp[s2[j]] > 0):
                tmp[s2[j]]-=1
                temps+=1
                j+=1
            
            if temps == l1:
                return True
            
            if temps>0:
                tmp=copy.deepcopy(mp)



            i=i+1
        
        return False
            



