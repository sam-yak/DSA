class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if not root:
       return None
    root.left, root.right = root.right , root.left 
    invert_tree(root.left)
    invert_tree(root.right)
    return root 
    

if __name__ == "__main__":
    # Build: 4(2(1,3), 7(6,9))
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    result = invert_tree(root)
    assert result.val == 4
    assert result.left.val == 7
    assert result.right.val == 2
    assert result.left.left.val == 9
    assert result.right.right.val == 1
    print("All tests passed!")
