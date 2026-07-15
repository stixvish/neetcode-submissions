class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        ml, mr = height[l], height[r]
        print(l, r, ml, mr)
        while l <= r:
            if ml <= mr:
                ans += ml - height[l] if ml - height[l] > 0 else 0
                ml = height[l] if height[l] > ml else ml
                l += 1
            else:
                ans += mr - height[r] if mr - height[r] > 0 else 0
                mr = height[r] if height[r] > mr else mr
                r -= 1
        return ans
