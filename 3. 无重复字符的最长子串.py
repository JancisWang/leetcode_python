'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        start = 0
        end = 0
        max_len = 0
        count = 0
        d = defaultdict(int)
        while end < len(s):
            if d[s[end]] > 0:
                count += 1
            d[s[end]] += 1
            end += 1
            while count > 0:
                if d[s[start]] > 1:
                    count -= 1
                d[s[start]] -= 1
                start += 1    
            max_len = max(max_len, end-start)
        return max_len
                
       

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ignore_index_end = -1
        d = {}
        max_len = 0
        
        for index, num in enumerate(s):
            if num in d and d[num] > ignore_index_end:
                ignore_index_end = d[num]
                d[num] = index
            else:
                d[num] = index
                max_len = max(max_len, index-ignore_index_end)
        return max_len




