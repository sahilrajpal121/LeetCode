class Solution: 
    def backspaceCompare(self, s: str, t: str) -> bool:
        s, t = s[::-1], t[::-1]
        
        def process(s: str) -> str:
            new = ''
            start = 0
            for ch in s:
                if ch == '#':
                    start += 1
                elif start:
                    start -= 1
                else:
                    new += ch
            return new
        
        
        s_new = process(s)
        t_new = process(t)
        
        print(s_new, t_new) #debug
        return s_new == t_new
                