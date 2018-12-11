#https://leetcode.com/problems/climbing-stairs/
#跟斐波那契数列结合是有点搞事情了，不过确实是斐波那契数列，但是递归最大的问题就是真的很费时间。
#网上有一个动态规划记录历史数据的方法，就是用一歌list把前面所有的值都记录下来。
#但是怎么感觉这个动态规划还是递归呢，总感觉跟递归没啥区别呀。
#这里用的是循环。
def climbStairs(n):
    a = 1
    b = 1
    for i in range(1,n):
        a , b = b , a+b
    return b
print(climbStairs(3))