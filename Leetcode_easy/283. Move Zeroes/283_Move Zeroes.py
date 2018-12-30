#https://leetcode.com/problems/move-zeroes/
def moveZeroes(nums):
    nums.sort()
    while 1 :
        if nums[0] == 0 :
            nums.pop(0)
            nums.append(0)
        else :
            break 
    print(nums)
moveZeroes([0,1,0,3,12])
#测试的时候也太扯了吧，给我一个全零的list让我排序，全是零排毛线的序，mmp！！！！