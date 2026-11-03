class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Approach 2: Counter 

        return Counter(nums).most_common(1)[0][0]
