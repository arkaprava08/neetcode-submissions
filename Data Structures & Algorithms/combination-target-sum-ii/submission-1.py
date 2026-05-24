class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        res1=[]
        out={}
        def helper(idx, runningSum, arr):
            if runningSum > target:
                return

            if runningSum == target:
                res1.append(arr.copy())
                out[tuple(sorted(arr.copy()))]=1

            for i in range(idx+1, len(candidates)):
                arr.append(candidates[i])
                helper(i, runningSum+candidates[i], arr)
                arr.pop()

        
        helper(-1, 0, [])

        for k,v in out.items():
            res.append(list(k))

        print(res1)

        return res