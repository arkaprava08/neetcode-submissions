class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals=sorted(intervals, key=lambda x:x[0])

        res=[]

        for inter in intervals:
            # print(res)
            if len(res)>0 and res[-1][1]>=inter[0]:
                # merge
                top=res.pop()
                res.append([top[0], max(top[1], inter[1])])
            else:
                res.append(inter)
            
        return res