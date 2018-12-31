#https://leetcode.com/problems/reverse-vowels-of-a-string/
def reverseVowels(s):
    strlist = [x for x in s]
    x = []
    for i in strlist :
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
           x.append(i)
           strlist[strlist.index(i)] = ' '   
    k = 0
    x.reverse()
    for j in strlist :
        if j == ' ' :
            strlist[strlist.index(j)] = x[k]
            k = k + 1
    s = ''
    for t in strlist :
        s = s + t
    return s
print(reverseVowels('leotcede')) 