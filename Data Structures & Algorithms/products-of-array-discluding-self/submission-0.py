class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, pos = [[0] * len(nums) for _ in range(2)]
        for i in range(len(nums)):
            pre[i] = (1 if i - 1 < 0 else pre[i-1]) * nums[i]
        for i in reversed(range(len(nums))):
            pos[i] = (1 if i + 1 >= len(nums) else pos[i+1]) * nums[i]
        # now use pre and post
        out = [0] * len(nums)
        for i in range(len(nums)):
            out[i] = (1 if i - 1 < 0 else pre[i-1]) * (1 if i + 1 >= len(nums) else pos[i+1])
        return out