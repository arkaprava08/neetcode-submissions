class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # print("arka: ", nums)
        self._k = k
        self._nums = []
        for i in nums:
            if len(self._nums) < k:
                heapq.heappush(self._nums, i)
            else:
                heapq.heappushpop(self._nums, i)
        # print("arka2: ", self._nums)

    def add(self, val: int) -> int:

        if len(self._nums) < self._k:
            heapq.heappush(self._nums, val)
        else:
            heapq.heappushpop(self._nums, val)

        print("out", self._nums[0])
        return self._nums[0]
        
