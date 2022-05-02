class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = len(nums) - 1
        i = 0 
        while i < j:
            if nums[i] & 1:
                if not nums[j] & 1:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j -= 1
            else: 
                i += 1
        print(i, j)
        return nums