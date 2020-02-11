'''
easy
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n-1, -1, -1):
            if s[i] != " ":
                count += 1
            else:
                if(count):
                    break
                
        return count


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = []
        for i in range(n-1, -1, -1):
            if s[i] != " ":
                count.append(i)
            elif len(count) > 0:
                count.append(i)
                return count[0] - count[-1]
        return len(count)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0:
            return 0
        temp = s.split(' ')
        if len(temp[-1])!= 0:
            return len(temp[-1])
        else:
            return self.lengthOfLastWord(" ".join(temp[:-1]))