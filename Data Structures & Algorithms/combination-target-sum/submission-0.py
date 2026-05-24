class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        out=[]
        def helper(idx, totSum, currList):
            if totSum == target:
                out.append(currList.copy())
                return
            
            if totSum > target:
                return
            
            for i in range(idx, len(nums)):
                currList.append(nums[i])
                helper(i, totSum+nums[i], currList)
                currList.pop()

        
        helper(0, 0, [])

        return out

#       2
#      2,5,6,9