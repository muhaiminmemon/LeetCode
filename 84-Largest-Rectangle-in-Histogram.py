class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rectangles = []
        stack = []
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                rectangles.append(h * width)
            stack.append(i)
        
        while stack:
            h = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            rectangles.append(h * width)
        
        return max(rectangles) if rectangles else 0

        