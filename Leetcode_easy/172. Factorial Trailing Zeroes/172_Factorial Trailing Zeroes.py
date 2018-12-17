#https://leetcode.com/problems/factorial-trailing-zeroes/
def trailingZeroes(n):
    num = 1
    for i in range(1,n+1) :
        num = num*i
    s = str(num)
    count = 0
    for j in s :
        if j == '0' :
            count = count + 1
    return count
print(trailingZeroes(5))