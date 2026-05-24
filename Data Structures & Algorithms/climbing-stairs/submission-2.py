class Solution:
    def __init__(self):
        self.dict=defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        
        if n-1 not in self.dict:
            self.dict[n-1]=self.climbStairs(n-1)

        if n-2 not in self.dict:
            self.dict[n-2]=self.climbStairs(n-2)

        return self.dict[n-1] + self.dict[n-2]
