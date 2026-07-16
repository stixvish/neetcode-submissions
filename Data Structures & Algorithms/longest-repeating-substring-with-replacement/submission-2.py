class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    freq = set(s)
    ans = 0
    for f in freq:
      l, x = 0, 0
      w = []
      for r in range(len(s)):
        w.append(s[r])
        if s[r] != f:
          x += 1
        while x > k:
          if w.pop(0) != f:
            x -= 1
          l += 1
        ans = max(ans, len(w))
    return ans
