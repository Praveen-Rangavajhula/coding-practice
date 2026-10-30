class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, num_i in enumerate(nums): 
            for j, num_j in enumerate(nums[i + 1:]):
                if num_j == target - num_i: 
                    return [i, j + i + 1]

        return None