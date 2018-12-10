#https://leetcode.com/problems/count-and-say/
#用递归来写，类似于数列an = f(an-1)的模式。
def temp(x):
    j = 0
    tmp = x[0]
    s = ''
    for i in range(0,len(x)+1) :#range()不包括stop点，range（0,5），输出的是01234五个数，没有5.
        if i <= len(x)-1 :
            if x[i] == tmp :
                j = j + 1
            else:
                s = s + str(j) + tmp 
                tmp = x[i]
                j = 1
        else :
            s = s + str(j) + tmp
    return s 

def countAndSay(n):
    p = ''
    if n == 1 :
        return '1'
    else :
        L = countAndSay(n-1)
        p = str(temp(L)) 
        return p
print(countAndSay(10))