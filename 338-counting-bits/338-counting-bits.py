class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0,1]
        if n <= 1:
            return ans[:n+1]
        
        for i in range(2,n+1):
            ref = i // 2
            if i & 1: 
                ans.append(ans[ref]+1)
            else:
                ans.append(ans[ref])
        return ans