class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Approach 1: Hashing 

        counts = defaultdict(int)

        for num in nums: 
            counts[num] += 1

        return sorted(counts, key=counts.get, reverse=True)[0]