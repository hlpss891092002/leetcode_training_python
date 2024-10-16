class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate_node(root, float("-inf"), float("-inf")) 
        # float("inf") positive infinite  float("-inf") negative infinite 
    def validate_node(self, root: TreeNode, min, max):
        if not root:
            return True
        # beyond leaf node 
        if root.val <= min or root.val >= max:
            return False
        # out of compare range
        return self.validate_node(root.left, min, root.val) and self.validate_node(root.right, root.val,max)
        #  Setting node.val as max of left subtree  and min of right subtree, then traverse subtrees ; 