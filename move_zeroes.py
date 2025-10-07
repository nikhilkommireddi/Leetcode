class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #sliding window approach 
        j = 0
        for i in range(len(nums)): 
            if num[i]!=0:
                temp = nums[j]                      
                nums[j] = num[i]
                nums[i] = temp
                j = j+1

    
    