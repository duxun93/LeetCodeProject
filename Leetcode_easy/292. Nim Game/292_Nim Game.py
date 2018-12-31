#https://leetcode.com/problems/nim-game/
#只要占住4的倍数的点就可以了，
#例如n = 100 ，那么我保证我开始拿的时候是97个-99个，
#这样的话我就要保证我上一次拿的时候是93-95个，以此类推，其实需要占住的点就是96这个点
#那么每次取得函数就可以为找4的点。
#推广到n，需要占得点就是n-4……
def canWinNim(n):
    k = 1
    j = 0
    point = n % 4
    L1 = []
    L2 = []
    tmp = [x for x in range(1,n+1)]
    for i in tmp :
        if j % 2 == 0 :
            if k < 3:
                if i != point :
                    L1.append(i)
                    k = k + 1
                else :
                    L1.append(i)
                    k = 1
                    j = j + 1
                    continue
            else :
                k = 1
                j = j + 1
        elif j % 2 == 1 :
            if k < 3 :
                if i != point :
                    L2.append(i)
                    k = k + 1
                else : 
                    L2.append(i)
                    k = 1 
                    j = j + 1
                    continue
    return L1,L2
print(canWinNim(100))
#还在纠结，没写好