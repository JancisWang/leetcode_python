'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
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
    def isSymmetric(self, root: TreeNode) -> bool:

        def ismirror(left, right):
            if not (left or right): return True
            if not (left and right): return False
            return (left.val==right.val) and ismirror(left.right,right.left) and ismirror(left.left, right.right)
            
        return ismirror(root, root)


# 迭代
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        nodes = [root, root]
        while nodes:
            t1 = nodes.pop()
            t2 = nodes.pop()
            if not (t1 or t2): continue;
            if not (t1 and t2): return False
            if not t1.val == t2.val: return False
            nodes.append(t1.left)
            nodes.append(t2.right)
            nodes.append(t1.right)
            nodes.append(t2.left)

        return True






        


       
