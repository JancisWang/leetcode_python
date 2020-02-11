'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visited = []
        stack = []
        def goAlongLeft(tree):
            while tree:
                stack.append(tree)
                tree = tree.left

        while stack or root:
            goAlongLeft(root)
            x = stack.pop()
            visited.append(x.val)
            root = x.right
        return visited


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if root:
                if root.left:
                    helper(root.left)
                res.append(root.val)
                if root.right:
                    helper(root.right)
        helper(root)
        return res





        

