#https://leetcode.com/problems/two-sum/
def twoSum(nums, target):
    print(type(nums))
    for i in nums:
        j = target - i
        if j in nums:
            print(i, j)
            nums.remove(i)
            nums.remove(j)
        else:
            continue
    return (i,j)
nums = [2, 7, 11, 15, 1, 8]
target = 9
twoSum(nums, target)