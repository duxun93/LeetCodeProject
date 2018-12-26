#https://leetcode.com/problems/happy-number/
#python字符串用的真是神奇，可以拿来直接拆数字。
def sumstr(s):
    l = str(s)
    m = 0
    for i in l :
        m = m + int(i)**2
    return m
def isHappy(n):
    dicsum = []
    while True :
        n = sumstr(n)  
        if n == 1 :
            return True
        elif n in dicsum :
            return False
        else :
            dicsum.append(n)
            continue
print(isHappy(19))  