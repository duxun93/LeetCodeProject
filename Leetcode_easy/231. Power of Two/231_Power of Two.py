#https://leetcode.com/problems/power-of-two/
def isPowerOfTwo(n):
    if n == 1:
        return True
    else :
        tmp = n 
        while 1:
            if tmp%2 != 0 :
                return False
            else :
                tmp = tmp / 2 
                if tmp == 2 :
                    return True
print(isPowerOfTwo(218))
print(isPowerOfTwo(16))