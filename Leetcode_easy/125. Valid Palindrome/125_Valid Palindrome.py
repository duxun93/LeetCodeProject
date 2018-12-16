#https://leetcode.com/problems/valid-palindrome/
#判断是不是回文的问题，忽略除了数字和字母以外的其他东西。
def isPalindrome(s):
    L = []
    P = []
    for i in s.lower() :
        if i.isdigit() or i.isalpha() :
            L.append(i)
    P = list(reversed(L))
    if P == L : 
        return True
    else :
        return False
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))