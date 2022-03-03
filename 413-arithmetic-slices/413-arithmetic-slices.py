class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return 0
        
        prev_diff = nums[1] - nums[0]
        s = 0
        curr = 0
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            
            if diff == prev_diff:
                curr += 1
            else:
                prev_diff = diff
                curr = 0
            
            s += curr
            
        return s