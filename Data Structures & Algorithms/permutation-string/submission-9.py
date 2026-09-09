import copy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l1,l2=len(s1),len(s2)

        mp=defaultdict(int)

        for ch in s1:
            mp[ch]+=1

        i=0

        while(i<(l2-l1+1)):
            print("START: ", i)
            j=i
            temps=0
            tmp=copy.deepcopy(mp)

            
            while(temps<l1 and s2[j] in tmp and tmp[s2[j]] > 0):
                # print("inner: i -> ", j, s2[j])
                tmp[s2[j]]-=1
                temps+=1
                j+=1
                # print("post inner: i -> ", j, s2[j], s2[j] in tmp, tmp[s2[j]] > 0)
            
            # print("AT: i -> ", i, s2[i]," and j -> ", j, s2[j], mp, tmp)
            # print("after run: ", temps, l1)
            if temps == l1:
                return True


            i=i+1
        
        return False
            



