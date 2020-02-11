'''
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4 
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。

在真实的面试中遇到过这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subtree-of-another-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: return True
        if not s: return False
        return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSame(self, s, t):
        if not t and not s: return True
        if not t or not s: return False
        return s.val==t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        ss = self.inorder(s)
        tt = self.inorder(t)
        return tt in ss
    
    def inorder(self, s):
        if not s: return '#'
        return '*' + str(s.val) + self.inorder(s.left) + self.inorder(s.right)


       

