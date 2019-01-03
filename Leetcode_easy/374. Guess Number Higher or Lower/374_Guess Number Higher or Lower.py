#https://leetcode.com/problems/guess-number-higher-or-lower/
def guessMe(n) : 
    if n > 6 :
        return 1
    elif n == 6 :
        return 0
    elif n < 6 :
        return -1
def guessNumber(self, n):
    if guessMe(n) == 0:
         return n
    elif guessMe(1) == 0 :
        return 1
    else:
        left = 1
        right = n
        point = n//2
        while 1:
            if guessMe(point) == 0 :
                return point
            elif guessMe(point) == 1 :
                left = point
                point = (point+right)//2
            elif guessMe(point) == -1 :
                right = point
                point = (point+left+1)//2
                