class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap=[]
        intMap=defaultdict(int)

        for i in nums:
            intMap[i]+=1

        for i,v in intMap.items():
            heap.append([-v, i])

        out=[]

        print(heap)

        for i in range(k):
            heapq.heapify(heap)
            out.append(heapq.heappop(heap)[1])

        return out