#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

def len_link(list):
    temp=list[0]
    count=0
    while(temp):
        count+=1
        temp=temp.next
    return count

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sol = []
        i = 0
        j = 0

        while i < len_link(list1) or j < len_link(list2):
            if list1[i] == list2[j]:
                sol.append(list1[i], list2[j])
                i += 1
                j += 1
            elif list1[i] < list2[j]:
                sol.append(list1[i])
                i += 1
            else:
                sol.append(list2[j])
                j += 1
        return sol
                
            
# @lc code=end

