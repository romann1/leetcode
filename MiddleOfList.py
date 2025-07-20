class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: 'ListNode | None' = None

    @staticmethod
    def make_list(in_list) -> 'ListNode | None':
        head = ListNode(None)
        tail = ListNode(None)

        for x in in_list:
            node = ListNode(x)
            if head.val is None:
                head = node
                tail = head
            else:
                tail.next = node
                tail = node
        return head

    def __repr__(self):
        s = '['
        s = s + str(self.val) + ','
        node = self.next
        while node is not None:
            s = s + str(node.val) + ','
            node = node.next
        s = s[0:-1] + ']'

        return s


class Solution:
    def middleNode(self, head: 'ListNode | None') -> 'ListNode | None':
        ptr = head
        mid = head

        i = 0
        while ptr is not None:
            i += 1
            if i % 2 == 0 and mid is not None:
                mid = mid.next
            ptr = ptr.next

        return mid

sol = Solution()

res_list = sol.middleNode(ListNode.make_list([1, 2, 3, 4, 5]))
print(f'{res_list}')
res_list = sol.middleNode(ListNode.make_list([1, 2, 3, 4, 5, 6]))
print(f'{res_list}')