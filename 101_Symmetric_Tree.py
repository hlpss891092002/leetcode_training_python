class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        # none val also match symmetric
        return self.is_sym(root.left, root.right)
        # compare right and left subtree
    def is_sym(self, l: TreeNode, r: TreeNode):
        if not l and not r: #  both of nodes are empty 
            return True # match symmetric
        if not l or not r: #  one of nodes is empty
            return False # not match symmetric
        return l.val == r.val and self.is_sym(l.left, r.right) and self.is_sym(l.right, r.left)  
        # subtree match 
        # 1. value of right node == value of left node 
        # 2. left value of left subtree == right value of  right subtree
        # 3. right value of left subtree == left value of  right subtree