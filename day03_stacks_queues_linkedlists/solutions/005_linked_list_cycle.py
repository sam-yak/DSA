class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    # Test 1: cycle exists
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b      # cycle: 4 → 2
    assert has_cycle(a) == True

    # Test 2: no cycle
    x = ListNode(1, ListNode(2, ListNode(3)))
    assert has_cycle(x) == False

    print("All tests passed!")
