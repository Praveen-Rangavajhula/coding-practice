class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Method 1: Brute Force
        # Time Complexity: O(N^2)
        # Space Complexity: O(1)

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             if nums[i] == nums[j]:
        #                 return True

        # return False

        
        # Method 2: Sorted List
        # Time Complexity: O(N log(N))
        # Space Complexity: O(N) 
        
        # (Python uses Timsort internally which is O(N) worst case)

        # if nums:
        #     nums.sort()
        #     for i in range(len(nums)-1): 
        #         if nums[i] == nums[i + 1]:
        #             return True

        # return False

        # Method 3: Use Sets  
        # Time Complexity: O(N)
        # Space Complexity: O(N)

        # We could do it iteratively which would early return, 
        # but worst case would remain the same. 
        # We could also use a hashmap, or a dictionary 
        # as they're called in Python. 

        return len(nums) != len(set(nums))




