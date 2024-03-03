class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        head_p = head
        head_p2 = head
        for _ in range(n):
            head_p = head_p.next
        if not head_p:
            return head.next
        while head_p.next:
            head_p = head_p.next
            head_p2 = head_p2.next
        head_p2.next = head_p2.next.next
        return head
