'''
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

 



 

示例：

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
 

注意：

你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/keyboard-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = {'Q', 'W', 'E','R', 'T', 'Y', 'U', 'I', 'O', 'P'}
        row_2 = {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
        row_3 = {'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
        
        def match(row, string):
            string = set(string.upper())
            for s in string:
                if s not in row:
                    return False
            return True
        
        result = []
        for word in words:
            if match(row_1, word) or match(row_2, word) or match(row_3, word):
                result.append(word)
        return result