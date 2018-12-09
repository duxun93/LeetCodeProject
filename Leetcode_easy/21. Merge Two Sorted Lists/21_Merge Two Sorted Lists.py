#https://leetcode.com/problems/merge-two-sorted-lists/
def mergeTwoLists(l1, l2):
    L = []
    for i in l1:
        if i.isdigit() :
            L.append(i)
    for j in l2:
        if j.isdigit() :
            L.append(j)
    L = sorted(L)
    s = 's'
    for k in L :
        s = s + '->' + str(k)  
    print(s[3:])
mergeTwoLists('1->2->4', '1->3->4')