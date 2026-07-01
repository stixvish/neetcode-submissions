class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        ans = 0
        while i < j:
            ans = max((j - i) * min(heights[i], heights[j]), ans)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return ans