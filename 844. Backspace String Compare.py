'''
easy

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
'''

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        while S.find('#')!=-1:
            index = S.find('#')
            if index == 0: S = S[1:]
            else:
                S = S[:index-1] + S[index+1:]
        while T.find('#')!=-1:
            index = T.find('#')
            if index == 0: T = T[1:]
            else:
                T = T[:index-1] + T[index+1:]
        return S==T


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_ = ""
        T_ = ""
        for i in S:
            if i=="#": S_ = S_[:-1]
            else: S_ += i
        for j in T:
            if j == "#": T_ = T_[:-1]
            else: T_ += j
        return S_ == T_

        