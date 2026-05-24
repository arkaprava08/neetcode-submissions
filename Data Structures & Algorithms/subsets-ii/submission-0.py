class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        dict={}
        def helper(idx, arr):

            dict[tuple(sorted(arr))]=1

            
            for i in range(idx+1, len(nums)):
                arr.append(nums[i])
                helper(i, arr)
                arr.pop()

        
        helper(-1, [])

        res=[]
        for k,v in dict.items():
            res.append(list(k))

        return res
        