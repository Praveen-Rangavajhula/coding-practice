class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        for num in nums:
            if num != val:
                nums[start] = num
                start += 1
        return start