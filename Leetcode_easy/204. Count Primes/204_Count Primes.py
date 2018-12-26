#https://leetcode.com/problems/count-primes/
def countPrimes(n):
    #找质数的问题，暴力法是最简单的。
    j = 0
    for i in range(2,n):
        if isprime(i) :
            j = j + 1
        else :
            continue
    return j
def isprime(x):
    if x == 1 or x == 4 :
        return False
    elif x == 2 or x == 3 or x == 5 :
        return True
    else :
        for i in range(1,x//2) :
            if i !=1 and x%i == 0 :
                return False
        return True
print(countPrimes(15))