class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            r = r + str(len(s)) + "#" + s
        return r

    def decode(self, s: str) -> List[str]:
        strs = []
        while s:
            index = 0
            for i, c in enumerate(s):
                if c == '#':
                    index = i
                    break
            count = int(s[0:index])
            strs.append(s[index+1:count+index+1])
            s = s[count+index+1:]
        return strs

            
            
        
            

