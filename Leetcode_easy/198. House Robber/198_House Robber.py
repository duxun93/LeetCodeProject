#https://leetcode.com/problems/house-robber/
def rob(nums):
    #年纪轻轻教我们抢劫，嗯，有意思。。。
    #可以这么理解，从第一个开始，然后把list里面相邻的pop出去，然后再开始找下一个，再pop出相邻的两个。
    #我用的是循环动态规划
    if len(nums) == 0 :
        return 0
    elif len(nums) == 1 :
        return nums[0]
    else :
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)) :
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[len(nums)-1]
print(rob([2,7,9,3,1]))