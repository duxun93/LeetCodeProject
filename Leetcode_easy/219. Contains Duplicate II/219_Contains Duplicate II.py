#https://leetcode.com/problems/contains-duplicate-ii/
#用enumerate()生成一个列表包含index的list ，
#然后用sort函数排序，这样原来list里面的index就不会被改变，然后再找index差值就好了
def containsNearbyDuplicate(nums, k):
    numslist = list(enumerate(nums))
    tmp = sorted(numslist,key = lambda x : x[1])
    for i in range(0,len(tmp)-1) :
        if tmp[i][1] == tmp[i+1][1] :
            if tmp[i+1][0] - tmp[i][0] <= k :
                return True
    return False
print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
print(containsNearbyDuplicate(nums = [1,0,1,1], k = 1))