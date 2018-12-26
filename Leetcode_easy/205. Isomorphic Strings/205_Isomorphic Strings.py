#https://leetcode.com/problems/isomorphic-strings/
def isIsomorphic(s,t):
    dic = {}
    for i,j in zip(s,t) :
        if i in dic :
            if dic[i] != j :
                return False
        else :
            dic[i] = j
    return True
print(isIsomorphic("egg","add"))
print(isIsomorphic(s = "foo", t = "bar"))