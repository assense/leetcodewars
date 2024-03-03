class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == nullptr) {
            return nullptr;
        }
        
        ListNode* head_p = head;
        ListNode* head_p2 = head;
        
        for (int i = 0; i < n; ++i) {
            head_p = head_p->next;
        }
        
        if (head_p == nullptr) {
            return head->next;
        }
        
        while (head_p->next != nullptr) {
            head_p = head_p->next;
            head_p2 = head_p2->next;
        }
        
        head_p2->next = head_p2->next->next;
        
        return head;
    }
};
