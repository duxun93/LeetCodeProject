#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
def twoSum(nums, target):
    P = list(i for i in nums)
    index = []
    for i in P:
        j = target - i
        if j in P:
            index1 = nums.index(i) + 1
            index2 = nums.index(j) + 1
            tup1 = (index1,index2)
            index.append(tup1)
            P.remove(i)
            P.remove(j)
        else:
            continue    
    return (index)
print(twoSum([2,7,11,15], target = 9))