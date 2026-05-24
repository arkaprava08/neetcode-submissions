class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        out=[0]*len(temperatures)
        val=0
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                curr=stack.pop()
                out[curr]=i-curr
            stack.append(i)

        return out