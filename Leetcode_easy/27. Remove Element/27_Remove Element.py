#https://leetcode.com/problems/remove-element/
def removeElement(nums, val):
    j = 0
    for i in nums :
        if i != val :
            j = j + 1
    return(j)
print(removeElement([0,1,2,2,3,0,4,2], val = 2))