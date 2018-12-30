#https://leetcode.com/problems/add-digits/
def addDigits(num):
    s = str(num)  
    while 1 :
        tmp = 0
        for i in s :
            tmp = tmp + int(i)
        s = str(tmp)
        if len(s) == 1 :
            return int(s)
print(addDigits(38))