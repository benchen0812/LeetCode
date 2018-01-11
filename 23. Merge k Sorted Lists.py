#23. Merge k Sorted Lists


# my solution
import heapq as hp
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        root = ns = ListNode(0)
        for i in range(len(lists)):
            if lists[i]:
                hp.heappush(h, (lists[i].val, i, lists[i]))
        
        while h:
            x = hp.heappop(h)
            ids = x[1]
            ns.next = ListNode(x[0])
            ns = ns.next
            if x[2].next:
                hp.heappush(h, (x[2].next.val, ids, x[2].next))
                
        return root.next


