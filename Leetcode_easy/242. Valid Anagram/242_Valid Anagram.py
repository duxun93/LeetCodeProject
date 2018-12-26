#https://leetcode.com/problems/valid-anagram/
def isAnagram(s,t):
    tmp1 = sorted(s)
    tmp2 = sorted(t)
    for i,j in zip(tmp1,tmp2) :
        if i != j :
            return False
    return True
print(isAnagram(s = "anagram", t = "nagaram"))
print(isAnagram(s = "rat", t = "car"))