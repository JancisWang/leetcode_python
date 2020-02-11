'''
Easy
Matrix Cells in Distance Order
We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), 
where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from 
smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) 
is the Manhattan distance, |r1 - r2| + |c1 - c2|.  
(You may return the answer in any order that satisfies this condition.)
'''

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        x = list(range(R))
        y = list(range(C))
        
        pair = [[x1, y1] for x1 in x for y1 in y]
        pair.sort(key = lambda x:abs(x[0]-r0)+abs(x[1]-c0))
        return pair