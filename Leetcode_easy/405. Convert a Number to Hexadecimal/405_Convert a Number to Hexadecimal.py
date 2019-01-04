#https://leetcode.com/problems/convert-a-number-to-hexadecimal/
def toHex(num):
    dicnum = {0:'0',1:'1',2:'2',3:'3',
              4:'4',5:'5',6:'6',7:'7',
              8:'8',9:'9',10:'a',11:'b',
              12:'c',13:'d',14:'e',15:'f'}
    strnum = ''
    if num > 0:
        while num > 15 :
            tmp1 = num//16
            tmp2 = num%16
            strnum = strnum + dicnum[tmp2]
            num = tmp1
        strnum = strnum + dicnum[num]
        return str(strnum[::-1])
    if num == 0:
        return '0'
    if num < 0 :
        num = ~int(bin(-num)[2:])#没有搞懂为什么1取反是-2
        print(num)
print(toHex(-1))