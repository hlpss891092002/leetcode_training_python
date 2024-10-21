class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#target : find the ancestor of p and q 
# find node between p and q
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val > p.val and root.val > q.val: # current node higher the p and q 
                root = root.left                      # current node move to lower node
            elif root.val < p.val and root.val < q.val: # current node lower the p and q 
                root = root.right                       # current node move to higher node
            else:
                return root #current note between p and q return the node