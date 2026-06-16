class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l=0
        rollingSum=0
        outlen=999
        found=False

        for r in range(len(nums)):
            rollingSum+=nums[r]

            while rollingSum >= target:
                found=True
                outlen=min(outlen, (r-l+1))

                rollingSum-=nums[l]
                l=l+1
            

        return outlen if found else 0



        