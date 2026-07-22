class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    # map s1
    s1_m = [0] * 26
    for c in s1:
        s1_m[ord(c) - ord('a')] += 1
    # sequentially map s1 length segments of s2
    for i in range(len(s2) - len(s1) + 1):
        s2_m = [0] * 26
        for c in s2[i:i+len(s1)]:
            s2_m[ord(c) - ord('a')] += 1
        if s1_m == s2_m:
            return True
    return False
