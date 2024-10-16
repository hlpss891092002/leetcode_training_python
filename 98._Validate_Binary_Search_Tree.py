class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._is_validBST(root, -2147483648, 2147483648)
    def _is_validBST(self, root: TreeNode, min, max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self._is_validBST(root.left, min, root.val) and self._is_validBST(root.right, root.val,max)