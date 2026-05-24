class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        closestKList=[]

        for point in points:
            dist=math.sqrt((point[0])*(point[0]) + (point[1])*(point[1]))
            heapq.heappush(closestKList, (dist, point))
        
        res=[]
        while k:
            res.append((heapq.heappop(closestKList)[1]))
            k-=1
        
        return res