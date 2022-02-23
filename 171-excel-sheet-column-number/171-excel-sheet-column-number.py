class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = reversed(columnTitle)
        a = ord("A") - 1
        ans = 0
        for i, ch in enumerate(columnTitle):
            diff = ord(ch) - a
            ans += 26 ** (i) * diff
        return ans