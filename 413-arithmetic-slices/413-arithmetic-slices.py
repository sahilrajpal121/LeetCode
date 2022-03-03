class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return 0
        
        subs = []
        for i in range(1, len(nums)-1):
            val = (nums[i] - nums[i-1]) == (nums[i+1] - nums[i])
            subs.append(val)
        
        curr = 0
        s = 0
        for sub in subs:
            if sub:
                curr += 1
            else:
                # if curr > 1:
                #     s += curr + 1
                # elif curr == 1:
                #     s += 1
                s += curr * (curr + 1) // 2
                curr = 0
        if curr:
            s += curr * (curr + 1) // 2
        return s     