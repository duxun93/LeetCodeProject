#https://leetcode.com/problems/add-strings/
def ddStrings(num1, num2):
    k = 0
    sumstr = []
    sumtmp = ''
    len1 = len(num1)
    len2 = len(num2)
    if len1 <= len2 :
        num1 = (len2-len1)*'0' + num1
        for i in range(len2-1,-1,-1) :
            if i != 0 :
                tmp = int(num1[i]) + int(num2[i]) + k 
                if tmp >= 10 :
                    tmp = tmp%10
                    k = 1
                else :
                    k = 0
                sumstr.append(str(tmp))
            else :
                tmp = int(num1[i]) + int(num2[i]) + k
                sumstr.append(str(tmp))
        sumtmp = ''
        sumstr.reverse()
        for i in sumstr :
            sumtmp = sumtmp + i
        return sumtmp
    elif len1 > len2 :
        num2 = (len1-len2)*'0' + num2
        for i in range(len1-1,-1,-1) :
            if i != 0 :
                tmp = int(num1[i]) + int(num2[i]) + k 
                if tmp >= 10 :
                    tmp = tmp%10
                    k = 1
                else :
                    k = 0
                sumstr.append(str(tmp))
            else :
                tmp = int(num1[i]) + int(num2[i]) + k
                sumstr.append(str(tmp))
        sumtmp = ''
        sumstr.reverse()
        for i in sumstr :
            sumtmp = sumtmp + i
        return sumtmp
print(ddStrings('123','456'))