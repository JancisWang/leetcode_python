'''
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

 

示例 1：



输入：[1,1,1,1,1,null,1]
输出：true
示例 2：



输入：[2,2,2,5,2]
输出：false
 

提示：

给定树的节点数范围是 [1, 100]。
每个节点的值都是整数，范围为 [0, 99] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/univalued-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        nodes = []
        def inorder(root):
            if root: 
                nodes.append(root.val)
                inorder(root.left)
                inorder(root.right)
        inorder(root)
        return len(set(nodes))==1


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        left_correct = (not root.left) or (root.left.val==root.val and self.isUnivalTree(root.left))
        right_correct = (not root.right) or (root.right.val==root.val and self.isUnivalTree(root.right))
        return left_correct and right_correct
 
        
