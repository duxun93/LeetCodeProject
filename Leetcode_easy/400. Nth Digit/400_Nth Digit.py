#https://leetcode.com/problems/nth-digit/
def findNthDigit(n):
        #巧用字符串，我觉得很好解。
    lis = ''
    for i in range(1,10) :
        if n > i*10**i-1 :
            n = n - i*10**(i-1)*9
        else :
            for j in range(10**(i-1),10**i) :
                lis = lis + str(j)
            return int(lis[n-1])
print(findNthDigit(1000))