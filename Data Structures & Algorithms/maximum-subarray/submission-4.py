class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSub=nums[0]
        currSum=0

        for i in range(0, len(nums)):
            if currSum<0:
                currSum=0
            currSum+=nums[i]
            maxSub=max(maxSub, currSum)


        return maxSub