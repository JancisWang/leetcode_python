'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.defaultdict(int)
        for i in s:
            d[i] += 1
        
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        else:
            return -1
        

class Solution:
    def firstUniqChar(self, s: str) -> int:
        min_index = len(s)

        for i in 'abcdefghijklmnopqrstuvwxyz':
            index = s.find(i)
            if index != -1 and s.rfind(i)==index:
                min_index = min(min_index, index)
        return min_index if min_index!=len(s) else -1