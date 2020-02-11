'''
easy

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
'''

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        alpha = [a for a in S if a.isalpha()]
        for i in range(-1, -len(S)-1, -1):
            if S[i].isalpha(): S[i] = alpha.pop(0)
        return "".join(S)


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i = 0
        j = len(S)-1
        S = list(S)
        while i < j:
            if S[i].isalpha() and S[j].isalpha():
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
            elif S[i].isalpha():
                j -= 1
            else:
                i += 1
        return "".join(S)


import re
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        i = 0
        j = len(s)-1
        if re.search('[A-Za-z]', S)==None: return S
        if len(re.findall('[A-Za-z]', S)) == 1: return S 
        while i < j:
            if re.search('[A-Za-z]', s[i]) != None and re.search('[A-Za-z]', s[j]) != None:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif re.search('[A-Za-z]', s[i]) != None:
                j -= 1
            else:
                i += 1
        return "".join(s)


                
            
        
        
        
