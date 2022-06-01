class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # search the first smaller num in the left side
        n = len(heights)
        stkL = [0]
        left = [-1] * n
        for i in range(n):
            while stkL and heights[stkL[-1]] >= heights[i]:
                stkL.pop()
            if stkL:
                left[i] = stkL[-1]
            stkL.append(i)
        # search the right index of a smaller number
        stkR = [n - 1]
        right = [n] * n
        for i in range(n - 1, -1, -1):
            while stkR and heights[stkR[-1]] >= heights[i]:
                stkR.pop()
            if stkR:
                right[i] = stkR[-1]
            stkR.append(i)
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, heights[i] * (right[i] - left[i] - 1))
        return maxArea