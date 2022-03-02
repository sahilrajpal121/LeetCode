class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True
        
        curr = 0
        limit = len(s)
        for i, ch in enumerate(t):
            if ch == s[curr]:
                curr += 1
            if curr == limit:
                return True