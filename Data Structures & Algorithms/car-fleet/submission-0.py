class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(a,b) for a,b in zip(position, speed)]
        pair.sort(reverse=True)

        stack=[]

        for a,b in pair:
            stack.append((target-a) / b)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)