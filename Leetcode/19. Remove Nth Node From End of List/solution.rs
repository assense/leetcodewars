impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut head = head;
        let mut head_p = head.as_mut();
        let mut head_p2 = head.as_mut();

        for _ in 0..n {
            head_p = head_p.unwrap().next.as_mut();
        }

        if head_p.is_none() {
            return head.unwrap().next;
        }

        let mut head_p = head_p.unwrap();

        while let Some(ref mut node) = head_p.next {
            head_p = node;
            head_p2 = head_p2.unwrap().next.as_mut().unwrap();
        }

        head_p2.unwrap().next = head_p2.unwrap().next.as_mut().unwrap().next.take();

        head
    }
}
