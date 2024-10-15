# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        
        result_code = ListNode() 
        result = result_code
        while list1 or list2  :
            if not list1:
                result_code.next = list2
                list2 = list2.next
            elif not list2:
                result_code.next = list1
                list1 = list1.next
            else:
                if list1.val <=  list2.val:
                    result_code.next = list1
                    list1 = list1.next
                else:
                    result_code.next = list2
                    list2 = list2.next
            result_code  = result_code.next
        return result.next