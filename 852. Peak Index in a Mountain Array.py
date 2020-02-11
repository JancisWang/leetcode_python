'''
easy

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
'''

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
       

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        temp = A[0]
        for i in range(1, len(A)):
            if A[i] > temp:
                temp = A[i]
            else: break
        return i-1
            
            
       
        