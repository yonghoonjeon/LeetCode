class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # calculate input s order using order
        res = ''
        for c in order:
            if c in s:
                cnt = s.count(c)
                s = s.replace(c, '')
                for i in range(cnt):
                    res += c
        # remain add
        res += s
        
        return res
            
                
        
        