'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = '0' * (len(a)-len(b)) + b
        elif len(a) < len(b):
            a = "0" * (len(b)-len(a)) + a
        
        summ = 0
        result = ""
        for i in range(len(a)-1, -1, -1):
            result = str((int(a[i]) + int(b[i]) + summ) % 2) + result
            summ = (int(a[i]) + int(b[i]) + summ) // 2 

        if summ > 0:
            result = "1" + result

        return result