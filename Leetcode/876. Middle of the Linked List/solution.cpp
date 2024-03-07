class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        if (!head) {
            return nullptr;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        while (true) {
            if (!fast->next) {
                return slow;
            }
            if (!fast->next->next) {
                return slow->next;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
    }
};
