class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        first_small = len(v1) <= len(v2) 
            
        for (n1, n2) in zip(v1, v2):
            if n1 < n2 : 
                return -1
            elif n1 > n2 :
                return 1
        
        if first_small : 
            biglist = v2
            curr = len(v1)
        else:
            biglist = v1
            curr = len(v2)
        
        
        for i in range(curr, len(biglist)):
            if biglist[i]:
                print('pakda gaya')
                if first_small:
                    return -1
                else:
                    return 1
                
        return 0