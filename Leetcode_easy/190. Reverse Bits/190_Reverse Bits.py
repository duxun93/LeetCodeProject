#https://leetcode.com/problems/reverse-bits/
def reverseBits(n):
    reversebit = ''
    s = str(n)
    tmp = list(reversed(s))
    for i in tmp :
        reversebit = reversebit + str(i)
    return reversebit
#问题是，tmp返回的是个二进制表示数值的字符串，至于怎么把引号去掉，还没有想到。
print(reverseBits('00000010100101000001111010011100'))