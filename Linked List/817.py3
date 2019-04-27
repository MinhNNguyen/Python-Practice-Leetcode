# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        numsList = [False] * 10000 
        cur, count, isConnected = head, 0, False
        for num in G:
            numsList[num] = True
        while cur:
            if numsList[cur.val]:
                isConnected = True
            else:
                if isConnected == True:
                    count += 1
                    isConnected = False
            cur = cur.next
        if isConnected == True:
            count += 1
        return count
            
        