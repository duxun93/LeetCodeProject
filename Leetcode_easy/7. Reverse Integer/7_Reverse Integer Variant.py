# if x wasn't define the range between -2^32--2^32-1
# how to solve this problem.
# 如果x范围没有限制，那么该如何解决。
def reverse(x):
    P = 0
    L = []
    if x > 0 :
        i = 0
        while 1:
            if divmod(x,10**(i+1))[0] != 0 or divmod(x,10**(i+1))[1] != x :#关键的条件，如何判断到最高位了，商为0，余数为x本身。
                L.append(x % 10**(i+1) // 10**i)
                i = i + 1
            else :
                L.append(x % 10**(i+1) // 10**i)
                break
        for n in range(0,len(L),1):
            j = len(L) - n -1
            P = P + L[n]*(10**j)
            n = n + 1
    else:
        x = -x
        i = 0
        while 1 :
            if divmod(x,10**(i+1))[0] != 0 or divmod(x,10**(i+1))[1] != x :
                L.append(x % 10**(i+1) // 10**i)
                i = i + 1
            else :
                L.append(x % 10**(i+1) // 10**i)
                break
        for n in range(0,len(L),1):
            j = len(L) - n -1
            P = P + L[n]*(10**j)
            n = n + 1
        P = -P 
    return(P)
print(reverse(-12345670000987621))