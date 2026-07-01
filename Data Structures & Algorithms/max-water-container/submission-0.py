class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        ans = 0
        while i < j:
            a = (j - i) * min(heights[i], heights[j])
            if a > ans:
                ans = a
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return ans