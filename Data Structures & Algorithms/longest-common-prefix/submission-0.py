class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mapOfPrefix={}
        for str in strs:

            tmp=""
            for i in range(len(str)):
                tmp+=str[i]
                if tmp not in mapOfPrefix:
                    mapOfPrefix[tmp]=0
                mapOfPrefix[tmp]+=1
        
        print(mapOfPrefix)
        maxPrefix=""
        for k,v in mapOfPrefix.items():
            if v == len(strs):
                maxPrefix=( k if len(k) > len(maxPrefix) else maxPrefix)

        return maxPrefix

