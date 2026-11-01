class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Approach 2: Sorting first

        # return sorted(set(nums), key=nums.count, reverse=True)[:k]
        # We get a TLE, worth a try though

        # I just looked at the official solution and they seem to be using
        # Min Heap! Let me try that

        cur = [0, nums[0]]
        heap = []
        nums = sorted(nums)

        for num in nums:
            if cur[1] == num:
                cur[0] += 1

            else:
                heapq.heappush(heap, cur)
                cur = [1, num]
                if len(heap) > k:
                    heapq.heappop(heap)

        heapq.heappush(heap, cur)
        cur = [1, num]
        if len(heap) > k:
            heapq.heappop(heap)

        ans = []

        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
