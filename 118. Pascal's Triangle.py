'''
easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def get_k(k):
            row = [1]
            for i in range(k):
                row.append((row[i] * (k-i))//(i+1))
                
            return row
        return [get_k(k) for k in range(numRows)]
            
            
        