class Solution:
    def __init__(self):
        self.dict=defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        
        if n-1 in self.dict:
            prev=self.dict[n-1]
        else:
            prev=self.climbStairs(n-1)
            self.dict[n-1]=prev

        if n-2 in self.dict:
            prevprev=self.dict[n-2]
        else:
            prevprev=self.climbStairs(n-2)
            self.dict[n-2]=prev
        return prev + prevprev
