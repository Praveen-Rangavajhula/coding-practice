class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Approach 1: Brute Force 

        product = 1
        switch = 0
        res = [0] * len(nums)

        for num in nums: 
            if num != 0: 
                product *= num 
            else: 
                switch += 1

            if switch > 1: 
                return res

        for i in range(len(nums)): 
            if switch == 1 and nums[i] == 0: 
                res[i] = product 
            elif switch == 0: 
                res[i] = int (product/nums[i])

        return res

        

        
        