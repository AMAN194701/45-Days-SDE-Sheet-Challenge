class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                if stack:
                    leftSmall = stack[-1]
                else:
                    leftSmall = -1

                rightSmall = i

                width = rightSmall - leftSmall - 1
                maxArea = max(maxArea, height * width)

            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            if stack:
                leftSmall = stack[-1]
            else:
                leftSmall = -1

            rightSmall = n
            width = rightSmall - leftSmall - 1
            maxArea = max(maxArea, height * width)

        return maxArea
        