class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = dict()
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            key = tuple(freq)
            if key not in hm.keys():
                hm[key] = []
            hm[key].append(s)
        return list(hm.values())