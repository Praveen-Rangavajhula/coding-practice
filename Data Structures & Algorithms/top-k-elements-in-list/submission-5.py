class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        return [num for num, _ in Counter(nums).most_common(k)]
        
        # Approach 3: Bucket sort 

        # buckets = [[] for i in range(len(nums) + 1)] # Create `n+1` buckets

        



