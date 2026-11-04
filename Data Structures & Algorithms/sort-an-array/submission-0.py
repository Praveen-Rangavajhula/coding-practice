class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Approach 1: Insertion Sort 
        # Time: O(n^2)
        # Space: O(1)

        for i in range(1, len(nums)):

            j = i - 1
            key = nums[i]

            while j >= 0 and nums[j] > key: 
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key

        return nums

            

