class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        leftMax=height[l]
        rightMax=height[r]
        out=0

        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax, height[l])
                out+=leftMax - height[l]
            else:
                r-=1
                rightMax=max(rightMax, height[r])
                out+=rightMax - height[r]


            
            
        return out
