class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mydict=defaultdict(list)

        for str in strs:
            count=[0]*26
            for c in str:
                count[ord(c) - ord('a')]+=1
            mydict[tuple(count)].append(str)
        


        out=list(mydict.values())
        print(mydict)
        
        return out
            