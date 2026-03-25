class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(3, ListNode(5)))
    l2 = ListNode(2, ListNode(4, ListNode(6)))
    result = merge_two_lists(l1, l2)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [1, 2, 3, 4, 5, 6]
    print("All tests passed!")
