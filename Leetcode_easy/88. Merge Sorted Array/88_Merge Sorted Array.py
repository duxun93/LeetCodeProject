#https://leetcode.com/problems/merge-sorted-array/
def merge(nums1, nums2):#我觉得m和n完全没用。
    #list.extend(seq)可以一次添加一个列表进去。
    nums1.extend(nums2)
    nums1.sort( )
    while 1:
        if 0 in nums1:
            nums1.remove(0)
        else:
            break
    return nums1
print(merge(nums1 = [1,2,3,0,0,0],nums2 = [2,5,6]))