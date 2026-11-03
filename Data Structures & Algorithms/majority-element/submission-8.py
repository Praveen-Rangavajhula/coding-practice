import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Approach 6: Random Selection
        
        # Las Vegas Randomized algorithm 

        n = len(nums)

        for num in nums: 
            candidate = random.choice(nums)

            if nums.count(candidate) > n // 2: 
                return candidate 

        