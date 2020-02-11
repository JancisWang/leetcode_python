'''
easy 
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
         

from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: return False
        d = Counter(nums)
        return max(list(d.values())) > 1

       
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for value in nums:
            if value not in d: d[value] = value
            else : return True
        return False
        
