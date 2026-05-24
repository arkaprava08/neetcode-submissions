class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea=0

        for i, h in enumerate(heights):
            while stack and h <= heights[stack[-1]]:
                top = stack.pop()
                maxArea=max(maxArea, heights[top]*(i-(stack[-1] if stack else -1) - 1))
            stack.append(i)
            print("arka - ", stack, maxArea)
        
        while stack:
            top=stack.pop()
            maxArea=max(maxArea, heights[top]*(i-(stack[-1] if stack else -1)))

        return maxArea