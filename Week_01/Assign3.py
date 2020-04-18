"""
合并两个有序链表
https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""

# 优化版本
class Solution:
    def mergeTwoLists(self, l1, l2):
        head =

# 原版本
class Solution2:
    def mergeTwoLists(self, l1, l2):
        head = None
        cur = head
        while l1 or l2:
            while l1 and (not l2 or l2.val >= l1.val):
                if not head:
                    head = l1
                    cur = head
                else:
                    head.next = l1
                    head = head.next
                l1 = l1.next

            while l2 and (not l1 or l1.val >= l2.val):
                if not head:
                    head = l2
                    cur = head
                else:
                    head.next = l2
                    head = head.next
                l2 = l2.next
        return cur

