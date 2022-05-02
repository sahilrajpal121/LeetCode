class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = len(nums) - 1
        i = 0 
        while i < j:
            if nums[i] & 1:
                if nums[j] & 1:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                    i += 1
            else: 
                i += 1
        print(i, j)
        return nums