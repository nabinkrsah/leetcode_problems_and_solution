"""1382. Balance a Binary Search Tree
Solved
Medium
Topics
Companies
Hint
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
    """




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        def sorted_list_to_bst(sorted_values, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(sorted_values[mid])
            node.left = sorted_list_to_bst(sorted_values, left, mid - 1)
            node.right = sorted_list_to_bst(sorted_values, mid + 1, right)
            return node
        
        sorted_values = inorder_traversal(root)
        return sorted_list_to_bst(sorted_values, 0, len(sorted_values) - 1)
