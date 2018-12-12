#https://leetcode.com/problems/pascals-triangle/
#杨辉三角，个人觉得用递归比较简单。
#当然循环也可以，可能代码复杂一些，但是要容易理解一些。
#这里用的是递归的方法。
def generate(numRows):
    for i in range(1,numRows+1):
        print(Yangtriangle(i))
def Yangtriangle(x):
    L1 = [1]
    L2 = [1,1]
    if x == 1 :
        return L1
    elif x == 2 :
        return L2
    else :
        L = [1]
        tmp = Yangtriangle(x-1)
        for i in range(0,len(tmp)-1) :
            L.append(tmp[i]+tmp[i+1])
        L.append(1)
        return L
generate(5)