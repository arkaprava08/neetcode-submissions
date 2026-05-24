class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        zero=0
        for i in nums:
            if i != 0:
                total=total*i 
            else:
                zero+=1
        out=[0]*len(nums)

        if zero>1:
            return out
        for i,j in enumerate(nums):
            if zero == 0:   
                out[i] = (total // j)
            else:
                out[i] = total if j == 0 else 0
        
        return out