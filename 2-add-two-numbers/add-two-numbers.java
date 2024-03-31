/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(((parse(l1) + parse(l2))%10));
        ListNode prev = head;
        ListNode curr = null;
        int carry = (parse(l1) + parse(l2))/10;
        l1 = l1.next;
        l2 = l2.next; 
        while(l1 != null || l2 != null) {
            int sum = parse(l1) + parse(l2) + carry;
            carry = sum/10;
            curr = new ListNode(sum%10);
            prev.next = curr;

            if(l1 != null) {l1 = l1.next;}
            if(l2 != null) {l2 = l2.next;}
            prev = prev.next;
            curr = curr.next; //null
        }
        if(carry != 0) {
            curr = new ListNode(carry);
            prev.next = curr;
        }

        return head;
    }

    public int parse(ListNode node) {
        if(node == null) {
            return 0;
        }
        else {
            return node.val;
        }
    }
}