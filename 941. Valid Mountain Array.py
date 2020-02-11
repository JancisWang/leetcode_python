'''
easy

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
'''

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) >= 3:
            diff = [a - b for a, b in zip(A[:-1], A[1:])]
            index_max = A.index(max(A))
            if index_max == 0 or index_max == len(A)-1:
                return False
            elif (max(diff[:index_max]) < 0) and (min(diff[index_max:])>0):
                return True
            else:
                return False
        else: 
            return False
       

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        i = 0
        j = n-1
        while i < j and A[i] < A[i+1]:
            i += 1
        while j > 0 and A[j] < A[j-1]:
            j -= 1
        if i == j and j!= n-1 and i!= 0:
            return True
        return False
        
       
