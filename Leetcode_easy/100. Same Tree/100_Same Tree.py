#https://leetcode.com/problems/same-tree/
def isSameTree(p, q):
    #我觉得这个题不是坑人呢么，最终变成两个列表比较，其实不就是列表中某一个值左侧和右侧两个值对应相等么。
    if len(p) == len(q) :
        if p[0] == q[0] :
            for i in range(1,len(p)) :
                if p[i] == q[i] and p[i-1] == q[i-1] and q[i+1] == p[i+1]:
                    return True
                else :
                    return False
        else :
            return False
    else :
        return False
# 个人觉得简书上的有一个博客写的很好，但是现在的我太菜，还没有懂，估计学会了怎么写类应该能懂。
#https://www.jianshu.com/p/32ef48c13640