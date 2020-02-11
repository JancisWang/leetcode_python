'''
Medium
 
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
'''

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ca = 0
        cb = 0
        string = ""
        while A or B:
            if A and ca < 2 and (A >= B or cb ==2):
                string += "a"
                ca += 1
                A -= 1
                cb = 0
            else:
                string += "b"
                cb += 1
                B -= 1
                ca = 0
        return string
            
        