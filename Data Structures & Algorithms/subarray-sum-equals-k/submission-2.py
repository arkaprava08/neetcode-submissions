class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixSum=[0]*(len(nums)+1)
        prefDict={0:1}
        res=0
        for i in range(1, len(prefixSum)):
            prefixSum[i]+=prefixSum[i-1]+nums[i-1]
            if (prefixSum[i]-k) in prefDict:
                res+=prefDict.get((prefixSum[i]-k), 0)
            prefDict[prefixSum[i]]=1+prefDict.get(prefixSum[i], 0)

        return res

