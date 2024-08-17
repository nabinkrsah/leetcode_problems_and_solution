'''1110. Delete Nodes And Return Forest
Solved
Medium
Topics
Companies
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete_set = set(to_delete)
        forest = []

        def helper(node, is_root):
            if not node:
                return None
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                forest.append(node)
            node.left = helper(node.left, root_deleted)
            node.right = helper(node.right, root_deleted)
            return None if root_deleted else node

        helper(root, True)
        return forest
