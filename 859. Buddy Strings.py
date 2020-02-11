'''
easy

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
'''

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if A==B and len(set(list(A)))!= len(A): return True
        result = []
        for i in range(len(A)):
            if A[i] != B[i]:
                result.append(i)
            if len(result) >= 3: return False
        if len(result) == 2 and A[result[0]]==B[result[1]] and A[result[1]]==B[result[0]]:
            return True
        else: return False
            
            
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):return False
        if A == B and len(set(A)) != len(A): return True
        value = [(a, b) for a, b in zip(list(A), list(B)) if a!=b]
        if len(value) ==2 and value[0][0] == value[1][1] and value[1][0] == value[0][1]: return True
        else: return False
            

        
                
            
        
                
            