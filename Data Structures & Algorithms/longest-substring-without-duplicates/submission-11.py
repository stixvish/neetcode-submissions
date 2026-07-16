class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, seen = 0, set()
        ans = 0
        for i in range(0, len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
                continue
            seen.add(s[i])
            ans = max(ans, len(seen))
        return ans

