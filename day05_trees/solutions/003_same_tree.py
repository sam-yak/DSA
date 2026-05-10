class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(t1, t2) == True

    t3 = TreeNode(1, TreeNode(2), None)
    t4 = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(t3, t4) == False

    assert is_same_tree(None, None) == True
    print("All tests passed!")
