class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        ml, mr = height[l], height[r]
        while l <= r:
            if ml <= mr:
                ans += max(ml - height[l], 0)
                ml = max(height[l], ml)
                l += 1
            else:
                ans += max(mr - height[r], 0)
                mr = max(height[r], mr)
                r -= 1
        return ans
