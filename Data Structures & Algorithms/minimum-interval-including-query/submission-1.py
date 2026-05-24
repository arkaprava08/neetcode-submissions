class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # l=[-1]*10001
        l=[-1]*10001

        res=[-1]*len(queries)

        for i in intervals:
            for j in range(i[0], i[1]+1):
                size=i[1]+1-i[0]
                l[j]=size if l[j] == -1 else min(l[j], size)
        
        for idx, q in enumerate(queries):
            res[idx] = l[q]
        
        return res