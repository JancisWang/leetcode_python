'''
easy

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i): return False
        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = list(ransomNote)
        m = list(magazine)
        for i in r:
            if i not in m: return False
            else: m.remove(i)
        return True
        
            
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine: return False
            else:magazine = magazine.replace(i,"", 1)
                
        return True
        
       
        
        