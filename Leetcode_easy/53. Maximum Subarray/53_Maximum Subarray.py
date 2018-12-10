#https://leetcode.com/problems/maximum-subarray/
#连续的子数组和。python中很好实现，暴力法就可以。
def countsum(x,y):#x为数列，y为相加数字的个数。
    L = []
    dictsum = {}
    for i in range(0,len(x)+1) :
        if i + y <= len(x) :
            L = tuple(x[i:i+y])
            dictsum[L] = sum(x[i:i+y])
        else :
            break
    return dictsum

def maxSubArray(nums):
    sum_dic = { }
    target = []
    for j in range(1,len(nums)) :
        M = countsum(nums,j)
        for key in M:
            sum_dic[key] = M[key]#把所有的值添加到一个dict中。
    summax = max(sum_dic.values())
    for k in sum_dic :
        if sum_dic[k] == summax:
            target.append(k)
    return(target,summax)
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))