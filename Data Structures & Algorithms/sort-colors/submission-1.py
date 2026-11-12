class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i, zero, one, two = 0, 0, 0, 0

        while two < len(nums):
            if nums[i] == 0:
                nums[i], nums[one] = nums[one], nums[i]
                nums[one], nums[zero] = nums[zero], nums[one]
                zero, one, two = zero + 1, one + 1, two + 1
                i = two
            elif nums[i] == 1:
                nums[i], nums[one] = nums[one], nums[i]
                one, two = one + 1, two + 1
                i = two
            else:
                nums[i], nums[two] = nums[two], nums[i]
                two += 1
                i = two