#https://leetcode.com/problems/single-number/
#排序，两两相减，单数的那个肯定相减不为0.
def singleNumber(nums):
    nums.sort()
    for i in range(0,len(nums),2) :
        if i != len(nums)-1 :
            if nums[i] - nums[i+1] == 0 :
                continue
            else :
                return nums[i]
        else :
            return nums[-1]
print(singleNumber([4,1,2,1,2]))
print(singleNumber([2,2,1]))