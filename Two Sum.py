class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # so we are given array of numbers , we have to return the indices of the sum of nums which are equal to target 
        output = {}   # we create an empty dict 
        for i in range(len(nums)):
            compliment = target - nums[i]  # this would give the compliment of the number we want to fil the sum for target
            if compliment in output:                       # if we found the compliment, 
                return output[compliment], i        # return both the current number index and compliment index 
            output[nums[i]]= i                     # if not add the curretn number and its index to the output 