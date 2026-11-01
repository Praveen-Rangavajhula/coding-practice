class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Btw, here's the one liner I was looking for.
        # return [num for num, _ in Counter(nums).most_common(k)]
        
        # Approach 3: Bucket sort 

        n = len(nums)
        buckets = [[] for i in range(n + 1)] # Create `n+1` buckets

        counts = {}

        for num in nums: 
            counts[num] = counts.get(num, 0) + 1

        for num, count in counts.items():
            buckets[count].append(num)

        ans = []

        for i in range(n, 0, -1):

            for num in buckets[i]:
                ans.append(num)

                if len(ans) == k: 
                    return ans

        return ans


        



