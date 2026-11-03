class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Approach 3: 
        # Let's think of an approach that's O(1) space and O(n) time
        # First, see the features of the majority element 

        # 1. Should occur at least ceil(n/2) times
        # 2. Also implies that when sorted, this will always be the middle element 
        # 3. In an unsorted array, you can go at max floor(n/2) places 
        #    without coming across this element 

        # Just received a hint, removing two elements that aren't equal will 
        # preserve the majority element. 

        i = 0
        j = 1

        while j < len(nums):
            if nums[i] != nums[j]:
                del nums[j]
                del nums[i]
            else: 
                i += 1 
                j += 1

        return nums[0]



