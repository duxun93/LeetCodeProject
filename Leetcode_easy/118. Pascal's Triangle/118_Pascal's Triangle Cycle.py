#这里用的是循环。
def generate(numRows):
    L = [[1],[1,1]]
    for i in range(2,numRows):
        tmp = L[i-1]
        L0 = [1]
        for j in range(0,len(tmp)-1) :
            L0.append(tmp[j]+tmp[j+1])
        L0.append(1)
        L.append(L0)
    return L
print(generate(5))