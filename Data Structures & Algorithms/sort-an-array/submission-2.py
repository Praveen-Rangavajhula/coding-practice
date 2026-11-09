class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Approach 2: Merge Sort 

        n = len(nums)
        
        if n <= 1: 
            return nums
        
        left = self.sortArray(nums[:n//2])
        right = self.sortArray(nums[n//2:])

        ans = [0] * n

        for i in range(n - 1, -1, -1): 
            
            if left and right:
                ans[i] = left.pop() if left[-1] > right[-1] else right.pop()
            elif len(right) == 0: 
                ans[i] = left.pop()
            elif len(left) == 0: 
                ans[i] = right.pop()

        return ans

        