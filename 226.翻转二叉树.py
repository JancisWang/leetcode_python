'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            temp = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = temp
        return root


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return root