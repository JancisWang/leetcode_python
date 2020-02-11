'''
您需要在二叉树的每一行中找到最大的值。

示例：

输入: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

输出: [1, 3, 9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 二叉树的层次遍历
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return 
        stack = [root]
        result = []
        while stack:
            max_now = float('-inf')
            n = len(stack)
            for _ in range(n):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                max_now = max(max_now, node.val)
            result.append(max_now)
        return result


# 动态规划 + 哈希表

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        hashmap = {}
        def dfs(root, depth):
            if not root:
                return 
            if depth not in hashmap:
                hashmap[depth] = root.val
            else:
                hashmap[depth] = max(hashmap[depth], root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 1)
        return [hashmap[i] for i in hashmap]


