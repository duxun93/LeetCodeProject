#https://leetcode.com/problems/merge-two-sorted-lists/
def mergeTwoLists(l1, l2):
    L = []
    for i in l1:
        if i.isdigit() :
            L.append(i)
    for j in l2:
        if j.isdigit() :
            L.append(j)
    
mergeTwoLists('1->2->4', '1->3->4')