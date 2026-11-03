class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1: 
            return nums[0]

        i = 0 
        j = 1

        while j < len(nums): 
            if nums[j] != nums[i]:
                nums = nums[:i] + nums[j+1:]
                return self.majorityElement(nums)
            else: 
                i += 1 
                j += 1 
        
        return nums[0]


