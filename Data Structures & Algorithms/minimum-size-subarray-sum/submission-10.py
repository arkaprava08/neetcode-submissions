class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l,r=0,0
        s=0
        out=999
        found=False

        print(nums)

        for r in range(len(nums)):

            s+=nums[r]
            if s >= target:
                found=True
                out=min(out, r-l+1)

                while s >= target:
                    out=min(out, r-l+1)
                    s-=nums[l]
                    l+=1
        
        return out if found else 0


        