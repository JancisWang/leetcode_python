'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        beg = 0
        end = 0
        n = len(s)

        for i in range(n):
            len1 = self.check(s, i, i)
            len2 = self.check(s, i, i+1)
            length = max(len1, len2)
            if length > end-beg:
                beg = i - (length-1) // 2
                end = i + length // 2
        return s[beg:end+1]

    def check(self, string, left, right):
        while left >= 0 and right < len(string) and string[left]==string[right]:
            left -= 1
            right += 1
        return right - left - 1

        
