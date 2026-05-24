class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freqMap=defaultdict(int)

        for num in nums:
            freqMap[num]+=1

        maxFreq=nums[0]
        for k,v in freqMap.items():
            if freqMap[maxFreq] < v:
                maxFreq=k
        
        return maxFreq

