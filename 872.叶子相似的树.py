'''
请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。



举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

 

提示：

给定的两颗树可能会有 1 到 100 个结点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/leaf-similar-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
        return list(dfs(root1))==list(dfs(root2))


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        nums1 = []
        nums2 = []
        def find_leaf(root, nums):
            if root and not root.left and not root.right:
                nums.append(root.val)
            if root.left:
                find_leaf(root.left, nums)
            if root.right:
                find_leaf(root.right, nums)
            return nums
        return find_leaf(root1, nums1) == find_leaf(root2, nums2)
