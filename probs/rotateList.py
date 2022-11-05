# Given the head of a linked list, rotate the list to the right by k places.
# 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            count = 1
            nodeList = [head]
            while head.next is not None:
                head = head.next
                nodeList += [head]
                count += 1
            rotate = k % count
            head.next = nodeList[0]
            print(count-rotate-1, count-rotate, len(nodeList))
            nodeList[count - rotate - 1].next = None
            # return nodeList[0]
            if rotate:
                return nodeList[count - rotate]
            else:
                return nodeList[0]

if __name__ == '__main__':
    pass