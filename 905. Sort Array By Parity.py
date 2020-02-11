'''
easy

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

'''
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        temp = [a for a in A if a%2==0]
        temp += [a for a in A if a%2==1]
        return temp
        
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        temp = [a for a in A if a%2==0]
        temp += [a for a in A if a%2==1]
        return temp
        