#https://leetcode.com/problems/first-unique-character-in-a-string/
def firstUniqChar(s):
    tmp = []
    dic = {}
    for i in s :
        if i in dic :
            dic[i] = dic[i] + 1
        else :
            dic[i] = 1
    for j in dic :
        if dic[j] == 1 :
            tmp.append(s.index(j))
    if tmp == [] :
        return -1
    else : 
        return min(tmp)