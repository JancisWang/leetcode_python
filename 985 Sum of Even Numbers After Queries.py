'''
EASY
Sum of Even Numbers After Queries

We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.
'''

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum_A = sum([a for a in A if a % 2 ==0]) # sum origin even numbers
        result = []
        for val, index in queries:
            temp = A[index]
            A[index] += val
            if temp % 2 == 0:
                if val % 2==0:
                    sum_A += val
                else: 
                    sum_A -= temp
            else:
                if val % 2 ==1:
                    sum_A = sum_A + val + temp 
            result.append(sum_A)
            
        return result
            
        
        