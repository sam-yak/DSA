class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    def helper(node, low, high):
        if not node:
            return True
        if low >= node.val or node.val >= high:
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    return helper(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    # Valid BST
    root1 = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7))
    assert is_valid_bst(root1) == True

    # Invalid BST (6 in left subtree of 5)
    root2 = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(7))
    assert is_valid_bst(root2) == False

    assert is_valid_bst(None) == True
    print("All tests passed!")
