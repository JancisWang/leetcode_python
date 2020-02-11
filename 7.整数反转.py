'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def reverse(self, x: int) -> int:
        sign = False
        if x < 0:
            sign = True
            x = x * -1
        x = int(str(x)[::-1])
        if sign:
            x = x * -1
        if x > 2**31-1 or x < -2**31:
            return 0
        else:
            return x
            

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num = x * -1
        else:
            num = x
        
        threshold = 1<<31 if x < 0 else (1<<31)-1
        res = 0
        while num != 0:
            res = res * 10 + num % 10
            num = num // 10
            if res > threshold:
                return 0
        return res if x> 0 else res*-1