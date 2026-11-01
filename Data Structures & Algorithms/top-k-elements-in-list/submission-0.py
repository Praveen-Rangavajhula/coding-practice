class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Approach 1: Hashing

        counts = defaultdict(int)

        for num in nums: 
            counts[num] += 1 

        return sorted(counts, key=counts.get, reverse=True)[:k]
