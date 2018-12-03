#https://leetcode.com/problems/longest-common-prefix/
#找最长前缀，只需要从头开始比就好了。
def longestCommonPrefix(strs):
    str0 = strs[0]
    str1 = strs[1]
    str2 = strs[2]
    long = min(len(str0),len(str1),len(str2))
    temp = 'a' 
    for i in range (0,long-1):
        if str0[i] == str1[i] == str2[i] :
            temp = temp + str0[i]
        else :
            break 
    return temp[1:len(temp)]
print(longestCommonPrefix(["flower","flow","flight"]))