class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        closestKList=[]

        for point in points:
            dist=math.sqrt((point[0])*(point[0]) + (point[1])*(point[1]))*-1
            if len(closestKList) == k:
                if dist > closestKList[0][0]:
                    heapq.heappop(closestKList)
                    heapq.heappush(closestKList, (dist, point))
            else:
                heapq.heappush(closestKList, (dist, point))
        
        print(closestKList)
        res=[]
        while k:
            res.append((heapq.heappop(closestKList)[1]))
            k-=1
        
        return res