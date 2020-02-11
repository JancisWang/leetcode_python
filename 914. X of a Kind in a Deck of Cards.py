'''
easy

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
'''

import collections
from fractions import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = collections.Counter(deck)
        value = [value for _, value in d.items()]
        return reduce(gcd, value) != 1
   
     
        
from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = Counter(deck)
        value = list(d.values())
        min_value = min(value)
        for i in range(2, min_value+1):
            if all([v % i ==0 for v in value]): return True
        return False
            
            
        
        
   
        
