#https://leetcode.com/problems/add-binary/
#python has a function:bin(),can transform Decimal to Binary.
#也可以用暴力法，就是便利，详见：https://blog.csdn.net/qiubingcsdn/article/details/82263114
#enumerate()函数可以返回一个list 每个元素是一个元组，
#元组第一个量是原list的下标，第二个是原list对应位置的元素。
#list(enumerate(seasons)) = [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
#这个牛X了。之前代码都白写了。
#int 把其他进制转化为十进制，bin把其他进制转化为二进制。
def addBinary(a, b):
    a = int(a,2)
    b = int(b,2)
    return bin(a+b)[2:]
print(addBinary(a = "1010", b = "1011"))