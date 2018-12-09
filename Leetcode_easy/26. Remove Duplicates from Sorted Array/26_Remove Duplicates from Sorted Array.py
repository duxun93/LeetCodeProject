#https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/
def removeDuplicates(nums):
    nums = sorted(nums)
    L = []
    for i in nums :        
        if i not in L :
            L.append(i)
    return len(L)
print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))