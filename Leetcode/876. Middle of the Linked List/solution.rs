impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() {
            return None;
        }
        let mut slow = head.clone();
        let mut fast = head.clone();
        loop {
            if fast.as_ref()?.next.is_none() {
                return slow;
            }
            if fast.as_ref()?.next.as_ref()?.next.is_none() {
                return slow.as_mut()?.next.take();
            }
            slow = slow?.next;
            fast = fast?.next?.next;
        }
    }
}
