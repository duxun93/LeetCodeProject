#这里用的是递归，参考网上的动态规划的方法。
def climbStairs(n):
    if n == 1 or n == 2 :
        return n
    else :
        step = [1,1]
        for i in range(2,n+1):
            step.append(step[i-1]+step[i-2])
        return step[n]
print(climbStairs(4))