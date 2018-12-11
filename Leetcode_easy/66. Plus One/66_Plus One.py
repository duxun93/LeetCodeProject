#https://leetcode.com/problems/plus-one/
#csdn上说是大数加法，给一个数组组成一个数，然后加一在拆成数组。
#Are you kidding me ?
def plusOne(digits):
    s = 0
    digits.reverse()
    for i in range(0,len(digits)) :
        s = s + digits[i] * (10 ** i)
    s = s + 1
    s = str(s)
    L = []
    for j in s :
        L.append(int(j))
    return L
print(plusOne([4,3,2,1]))
print(plusOne([1,2,3]))