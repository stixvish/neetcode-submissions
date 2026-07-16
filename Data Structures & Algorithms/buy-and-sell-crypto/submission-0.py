class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy is l, sell is r
        ans, l, r = 0, 0, 1
        while r < len(prices):
            print(ans, l, r)
            if prices[l] >= prices[r]:
                l = r
                r = l + 1
            else:
                ans = max(ans, prices[r] - prices[l])
                r += 1
        return ans