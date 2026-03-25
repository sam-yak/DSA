class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

if __name__ == "__main__":
    # Build: 1 → 2 → 3 → 4 → 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # Reverse: 5 → 4 → 3 → 2 → 1
    result = reverse_list(head)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [5, 4, 3, 2, 1]
    print("All tests passed!")
