#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#可以借用第53题的方法，求连续的子数组和，把相邻两天的差值求出来，然后找到差值中和最大的。
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
def maxProfit(prices):
    pricesList = []
    for i in range(0,len(prices)-1) :
        pricesList.append(prices[i+1]-prices[i])
    print(maxSubArray(pricesList)[-1])
maxProfit([7,1,5,3,6,4])