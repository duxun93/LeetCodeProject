#https://leetcode.com/problems/number-of-1-bits/
#python 字符串是个神器，都变成字符串迭代就ok。
def hammingWeight(n):
    s = str(n)
    j = 0
    for i in s :
        if i == '1' :
            j = j + 1 
    return j
print(hammingWeight(11111111111111111111111111111101))