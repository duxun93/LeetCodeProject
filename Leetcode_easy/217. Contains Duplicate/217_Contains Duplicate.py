#https://leetcode.com/problems/contains-duplicate/
#我想到了两种方法：
# 第一个是，我循环从list里面拿数，拿出以后pop这个数，判断原列表是否还有；
# 第二是从列表里面去数，取出以后放入另一个list，每次取数都去新建的list里面查找一下是否已经有了。
def containsDuplicate1(nums):
    for i in reversed(range(0,len(nums))) :
        tmp = nums.pop(i)
        if tmp in nums :
            return True
    return False

def containsDuplicate2(nums):
    tmp = []
    for i in nums :
        if i in tmp :
            return True
        else :
            tmp.append(i)
    return False

print(containsDuplicate1([1,2,3,1]))
print(containsDuplicate1([1,2,3,4]))
print(containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))
print(containsDuplicate2([1,2,3,4]))