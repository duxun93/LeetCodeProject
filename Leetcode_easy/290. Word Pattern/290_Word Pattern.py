#https://leetcode.com/problems/word-pattern/
def wordPattern(pattern, strs):
    dic = {}
    tmp = strs.split(' ')
    if len(pattern) != len(tmp) :
        return False
    else:
        for i,j in zip(pattern,tmp) :
            if i not in dic and j not in list(dic.values()) :
                dic[i] = j
            elif i in dic and dic[i] != j :
                return False
            elif list(dic.keys())[list(dic.values()).index(j)] != i:
                return False
    return True
print(wordPattern(pattern = "abba", strs = "dog dog dog dog"))