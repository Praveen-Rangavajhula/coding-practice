class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # return nums * 2

        # Without using built-in stuff 
        
        n = len(nums)
        ans = [0] * 2 * n

        for i in range(n): 
            ans[i] = ans[i + n] = nums[i]

        return ans
        