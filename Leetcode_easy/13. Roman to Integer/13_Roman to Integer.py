#https://leetcode.com/problems/roman-to-integer/
#MCMXCIV M = 1000, CM = 900, XC = 90 and IV = 4.
#python3 exec()可以用于对字符串赋值。
def romanToInt(s):
    datadic = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    L = []
    P = 0
    for x in s:
        L.append(x)
    for i in range(0,len(L)-1):
        if datadic[L[i]] >= datadic[L[i+1]]:
            P = P + datadic[L[i]]
        else :
            P = P - datadic[L[i]]
    P = P + datadic[L[len(L)-1]]
    return(P)
print(romanToInt('MCMXCIV'))

