class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s, t = s[::-1], t[::-1]
        s_new, t_new = '', ''
        
        start = 0
        for ch in s:
            if ch == '#':
                start += 1
            elif start:
                start -= 1
            else:
                s_new += ch
        
        start = 0
        for ch in t:
            if ch == '#':
                start += 1
            elif start:
                start -= 1
            else:
                t_new += ch
        
        print(s_new, t_new) #debug
        return s_new == t_new
                