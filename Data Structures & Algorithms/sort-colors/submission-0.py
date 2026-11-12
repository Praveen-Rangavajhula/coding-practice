class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counter = [0] * 3

        for num in nums: 
            counter[num] += 1

        val = 0

        for i in range(len(nums)):

            while counter[val] <= 0: 
                val += 1

            nums[i] = val
            counter[val] -= 1

        



