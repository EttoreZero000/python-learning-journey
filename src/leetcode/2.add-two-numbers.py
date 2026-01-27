#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        i = 0
        flag = False

        while l1 is not None:
            num1 += l1.val * 10**i
            l1 = l1.next
            i += 1




        num2 = 0
        i = 0
        flag = False

        while l2 is not None:
            num2 += l2.val * 10**i
            l2 = l2.next
            i += 1

            

        ultimo = None

        for num in str(num1 + num2):
            ultimo = ListNode(int(num), ultimo)

        return ultimo


        
# @lc code=end

