'''
easy

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
'''

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        j = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                j = i
            if count >= 2: return False
        if j==0 or j==len(nums)-2 or count==0: return True
        elif nums[j-1] <= nums[j+1] or nums[j] <= nums[j+2]: return True
        else: return False
            
            
               


        