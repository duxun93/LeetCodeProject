#https://leetcode.com/problems/rotate-array/
def rotate(nums, k):
    for i in range(0,k):
        s = nums.pop()
        nums.insert(0,s)#insert(x,y)对应列表index=x的位置插入y元素
    return nums
print(rotate([1,2,3,4,5,6,7],3))