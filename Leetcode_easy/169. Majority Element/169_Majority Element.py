#https://leetcode.com/problems/majority-element/
def majorityElement(nums):
    L = sorted(nums)
    P = {}
    for i in L :
        if i in P :#等同于 if P.__contains__(i):
            P[i] = P[i] + 1
        else :
            P[i] = 1 
    j = max(P.values())
    for x in P :
        if P[x] == j :
            return x
        else :
            continue
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([3,2,3]))