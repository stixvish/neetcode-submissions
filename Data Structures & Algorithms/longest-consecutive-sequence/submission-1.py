class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_r = 0
        for num in s:
            if num - 1 in s:
                continue
            cur_v = num
            r_len = 1
            while cur_v + 1 in s:
                r_len += 1
                cur_v += 1
            if r_len > max_r:
                max_r = r_len
        return max_r