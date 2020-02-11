'''
easy

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, value in enumerate(nums):
            if value not in d: d[value] = i
            elif i - d[value] <= k: return True
            else: d[value] = i
        return False

    
        
        
        