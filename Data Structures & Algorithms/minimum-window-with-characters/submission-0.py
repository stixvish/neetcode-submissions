class Solution:
  def minWindow(self, s: str, t: str) -> str:
    # easy return
    if len(t) > len(s):
      return ""
    # create maps
    have_map = dict()
    need_map = dict()
    for c in t:
      need_map[c] = need_map.get(c, 0) + 1
    for k in need_map:
      have_map[k] = 0
    need, have = len(need_map), 0
    # main logic
    ans = ""
    l = 0
    for r in range(len(s)):
        if s[r] in have_map:
            have_map[s[r]] += 1
            if have_map[s[r]] == need_map[s[r]]:
                have += 1
        while have == need:
            ans = s[l:r+1] if len(ans) > len(s[l:r+1]) or ans == "" else ans
            if s[l] in have_map:
                have_map[s[l]] -= 1
                if have_map[s[l]] < need_map[s[l]]:
                    have -= 1
            l += 1
    return ans
