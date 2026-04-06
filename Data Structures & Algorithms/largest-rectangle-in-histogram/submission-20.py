class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair (index, height)
        max_area = 0
        l = len(heights)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, (i - index) * height)
                start = index

            stack.append((start, h))

        for s in stack:
            max_area = max(max_area, (l - s[0]) * s[1])

        return max_area
            
