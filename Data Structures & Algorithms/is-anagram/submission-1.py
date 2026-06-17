class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # frequency table for s
        s_map = {}
        for letter in s:
            if letter not in s_map:
                s_map[letter] = 0
            s_map[letter] += 1
        # frequency table for t
        t_map = {}
        for letter in t:
            if letter not in t_map:
                t_map[letter] = 0
            t_map[letter] += 1
        # compare maps
        if (s_map == t_map):
            return True
        return False
