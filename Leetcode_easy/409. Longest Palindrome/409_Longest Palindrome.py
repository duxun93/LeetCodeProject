#https://leetcode.com/problems/longest-palindrome/
def longestPalindrome(s):
    dic = {}
    for i in s :
        if i in dic :
            dic[i] = dic[i] + 1
        else :
            dic[i] = 1
    k = 0
    v = 0
    for j in dic :
        if dic[j]%2 == 0 :
            v = v + dic[j]
        else :
            if k == 0 :
                v = v +dic[j]
                k = 1
            else :
                v = v + dic[j]-1
    return v