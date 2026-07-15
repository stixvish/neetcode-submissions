class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        for index, value in enumerate(height):
            maxL = max(height[0:index]) if height[0:index] else 0
            maxR = max(height[index+1:len(height)]) if height[index+1:len(height)] else 0
            trapped += min(maxL, maxR) - value if min(maxL, maxR) - value >= 0 else 0
        return trapped