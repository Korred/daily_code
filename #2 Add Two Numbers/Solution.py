class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        current = res = ListNode(0)
        while(l1 or l2 or carry):
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            current.next = ListNode(val)
            current = current.next
        return res.next


def lst_to_ln(lst):
    """
    List to ListNode conversion
    :type lst: List()
    :rtype: ListNode
    """
    ln = curr = ListNode(0)
    for i in lst:
        curr.next = ListNode(i)
        curr = curr.next
    return ln.next


def ln_to_lst(ln):
    """
    ListNode to List conversion
    :type lst: ListNode
    :rtype: List()
    """
    lst = []
    while(ln):
        lst.append(ln.val)
        ln = ln.next
    return lst


# Example use:
a = [2, 3, 4, 5]
b = [8, 7, 2, 9]
t = [0, 1, 7, 4, 1]

res = ln_to_lst(Solution().addTwoNumbers(lst_to_ln(a), lst_to_ln(b)))
print(res, res == t)
