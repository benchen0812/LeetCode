#my solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        ad = l1.val + l2.val
        if ad >9 :
            c = 1
            ad = ad -10
        new = ListNode(ad)
        return self.hp(l1.next, l2.next, c, new, new)
        
    def hp(self, l1, l2, c, nx, root):

        if l1 != None and l2 != None:
            ad = l1.val + l2.val + c
            if ad >9 :
                c = 1
                ad = ad -10
                nx.next = ListNode(ad)
            else:
                c = 0
                nx.next = ListNode(ad)
            return self.hp(l1.next, l2.next, c, nx.next, root)
        
        elif l1 != None:
            ad = l1.val + c
            if ad >9 :
                c = 1
                ad = ad -10
                nx.next = ListNode(ad)
            else:
                c = 0
                nx.next = ListNode(ad)
            return self.hp(l1.next, None, c, nx.next, root)
        
        elif l2 !=None:
            ad = l2.val + c
            if ad >9 :
                c = 1
                ad = ad -10
                nx.next = ListNode(ad)
            else:
                c = 0
                nx.next = ListNode(ad)
            return self.hp(None, l2.next, c, nx.next, root)
        
        else:
            if c != 0:
                nx.next = ListNode(c)
            return root

# other's solution
class Solution:
# @return a ListNode
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next