class MedianFinder:

    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]
        self.size=0


    def addNum(self, num: int) -> None:
        self.size+=1

        # First, add to maxHeap (represented with negative values)
        heapq.heappush(self.maxHeap, -num)
        
        # Move the largest of maxHeap to minHeap
        top = -heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, top)

        # Balance: minHeap can only have at most one more element than maxHeap
        if len(self.minHeap) > len(self.maxHeap)+1:
            top=heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -top)



    def findMedian(self) -> float:
        if self.size == 0:
            return 0

        elif self.size % 2 == 0:
            return (self.minHeap[0]+ -self.maxHeap[0])/2
        else:
            return self.minHeap[0]
        