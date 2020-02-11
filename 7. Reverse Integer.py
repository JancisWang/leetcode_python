'''
easy 

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)
            x = int(x[0] + x[1:][::-1])
            if x < -2 **31 : return 0
            return x
        else:
            x = int(str(x)[::-1])
            if x > 2**31-1: return 0
            return x


class Solution:
    def reverse(self, x: int) -> int:
        if x==0: return x
        x = str(x)
        flag = x.startswith('-')
        if flag: x = x[1:]
        x = x[::-1]
        
        if flag: x = "-" + x
        x = int(x)
        if x > 2**31-1 or x < -2**31: return 0
        return x