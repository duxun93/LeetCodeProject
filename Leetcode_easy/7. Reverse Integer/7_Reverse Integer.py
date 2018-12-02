#https://leetcode.com/problems/reverse-integer/
#x = L[0]*10^0+L[1]*10^1+......L[i]10^i
#P = L[i]*10^0+L[i-1]*10^1+....L[0]*10^i
def reverse(x):
    P = 0
    if x > (2**31-1) or x < (-2**31) :
        print ('error')
    else :
        L = []
        if x > 0 :
            for i in range(0,10):
                if divmod(x,10**(i+1))[0] != 0 or divmod(x,10**(i+1))[1] != x :
                    L.append(x % 10**(i+1) // 10**i)# 第10的i次幂系数
                    i = i + 1
                else :
                    L.append(x % 10**(i+1) // 10**i)# 第10的i次幂系数
                    break
            for n in range(0,len(L),1):
                j = len(L) - n -1
                P = P + L[n]*(10**j)
                n = n + 1
        else :
            x = -x
            for i in range(0,10):
                if divmod(x,10**(i+1))[0] != 0 or divmod(x,10**(i+1))[1] != x :
                    L.append(x % 10**(i+1) // 10**i)# 第10的i次幂系数
                    i = i + 1
                else :
                    L.append(x % 10**(i+1) // 10**i)# 第10的i次幂系数
                    break
            for n in range(0,len(L),1):
                j = len(L) - n -1
                P = P + L[n]*(10**j)
                n = n + 1
            P = -P            
    return(P)
print(reverse(-123000))
