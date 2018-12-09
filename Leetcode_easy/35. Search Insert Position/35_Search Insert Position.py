#https://leetcode.com/problems/search-insert-position/
def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else :
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)
print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))
#I have to say ,python has a lot of function available.
#If I use C/C++, coding needs lots of 'for' and 'if'. 
#But not difficult to solve.