'''
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.
'''

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        s = 0
        A.sort(reverse = True)
        while len(A) >= 3:
            if (A[0] < A[1] + A[2]) and (A[0] - A[2] < A[1]):
                s = sum(A[:3])
                break
            else:
                A = A[1:]
            
        return s
        
                
                
