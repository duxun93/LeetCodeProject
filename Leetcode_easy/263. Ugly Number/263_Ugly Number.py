#https://leetcode.com/problems/ugly-number/
#https://blog.csdn.net/coder_orz/article/details/51317748
#网上给出了三种方法。
def isUgly1(num):
    for i in [2,3,5] :
        while num % i == 0:
            num = num / i
        return True if num == 1 else False
def isUgly2(num):
    if num == 1 : 
        return True
    elif num % 2 == 0 :
        return isUgly2(num/2)
    elif num % 3 == 0 :
        return isUgly2(num/3)
    elif num % 5 == 0 :
        return isUgly2(num/5)
    else :
        return False
print(isUgly1(8))
print(isUgly1(121))
print(isUgly2(6))
print(isUgly2(196))