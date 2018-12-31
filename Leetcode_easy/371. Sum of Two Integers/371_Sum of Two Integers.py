#https://leetcode.com/problems/sum-of-two-integers/
#不让用加减，本来想的是，计数可以么？
#更有效的方法是用补码运算。
#正数补码等于它本身，负数补码等于符号位以后的数字取反加一
def getSum(a, b):
    while b != 0:
                carry = a & b
                a = (a ^ b) % 0x100000000
                b = (carry << 1) % 0x100000000
    return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)