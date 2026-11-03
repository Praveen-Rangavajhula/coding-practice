class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        temp = []

        for num in nums: 
            if num != val: 
                temp.append(num)

        n = len(temp)

        for i in range(n): 
            nums[i] = temp[i]

        return n

        


        

