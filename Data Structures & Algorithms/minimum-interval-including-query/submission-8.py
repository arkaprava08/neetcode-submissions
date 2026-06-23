class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        MAX=99999
        tmp=[MAX]*10001

        for interval in intervals:
            gap=(interval[1]-interval[0])+1
            for i in range(interval[0], interval[1]+1):
                tmp[i]=min(tmp[i], gap)

        out=[]
        for query in queries:
            if tmp[query] != MAX:
                out.append(tmp[query])
            else:
                out.append(-1)

        return out
            
        