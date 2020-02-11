'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: 
            return 0
        d_l = self.maxDepth(root.left)
        d_r = self.maxDepth(root.right)
        return 1 + max(d_l, d_r)



# 迭代
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root:
            stack.append((1, root))
        maxd = 0
        while stack:
            currentd, root = stack.pop()
            if root:
                maxd = max(maxd, currentd)
                stack.append((currentd+1, root.left))
                stack.append((currentd + 1, root.right))
        return maxd


