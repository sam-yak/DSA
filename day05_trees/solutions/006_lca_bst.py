class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    return root

if __name__ == "__main__":
    root = TreeNode(6,
        TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9)))
    p = root.left           # node 2
    q = root.right          # node 8
    assert lowest_common_ancestor(root, p, q).val == 6

    p = root.left           # node 2
    q = root.left.right     # node 4
    assert lowest_common_ancestor(root, p, q).val == 2

    p = root.left.right.left   # node 3
    q = root.left.right.right  # node 5
    assert lowest_common_ancestor(root, p, q).val == 4
    print("All tests passed!")
