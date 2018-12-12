#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
def deleteDuplicates(head):
    L = [ ]
    for i in head :
        if i.isdigit():
            if i in L :
                continue
            else :
                L.append(i)
    liststr = ''
    for j in L :
        liststr = liststr + '->' + j 
    return liststr[2:]
print(deleteDuplicates('1->1->2->3->3'))