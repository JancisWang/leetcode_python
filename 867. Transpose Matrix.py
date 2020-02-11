'''
easy

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
'''

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return map(list, zip(*A))

import numpy as np
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return np.transpose(A)
        


