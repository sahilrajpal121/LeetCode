class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = m-1, n-1
        from math import comb
        return comb(m+n, m)