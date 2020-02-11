'''
easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex ==0 : return [1]
        elif rowIndex == 1:return [1, 1]
        else:
            result = [1, 1]
            for i in range(2, rowIndex+1):
                temp = [result[j]+result[j+1] for j in range(len(result)-1)]
                result = [1] + temp + [1]
            return result
    
'''
the ith element of the kth row of Pascal's triangle is the binomial coefficient
C(k, i)

the i+1 th is C(k, i+1)
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row.append((row[i] * (rowIndex-i))//(i+1))
        return row


                
                
                
            
        
        
