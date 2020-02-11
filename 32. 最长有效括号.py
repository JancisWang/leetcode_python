'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 动态规划
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        ans = 0
        for i in range(1, len(s)):
            if s[i]==')' and s[i-1]=='(':
                if i >= 2:
                    dp[i] = dp[i-2] + 2
                else:
                    dp[i] = 2
            elif s[i]==")" and s[i-1]==')':
                if i - dp[i-1] - 1 >= 0:
                    if s[i - dp[i-1] - 1] == '(':
                        if i - dp[i-1] - 2 >= 0:
                            dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                        else: 
                            dp[i]= dp[i-1] + 2
            ans = max(ans, dp[i])
        return ans

# 使用栈
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)
        count = 0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    count = max(count, i - stack[-1])
        return count


# 不使用额外空间
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        max_count = 0
        for i in s:
            if i=="(":
                left += 1
            else:
                right += 1
            if left == right:
                max_count = max(max_count, right * 2)
            if right > left:
                left = right = 0
        left = right = 0
        for i in s[::-1]:
            if i == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_count = max(max_count, left * 2)
            if left > right:
                left = right = 0

        return max_count


# 超时
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def isvalid(string):
            stack = []
            for s in string:
                if s == "(":
                    stack.append(s)
                elif stack:
                    stack.pop()
                else:
                    return False
            return len(stack)==0
        
        max_count = 0
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if isvalid(s[i:j+1]):
                    max_count = max(max_count, j-i+1)
        return max_count