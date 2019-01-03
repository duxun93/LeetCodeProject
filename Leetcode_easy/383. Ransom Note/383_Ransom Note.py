#https://leetcode.com/problems/ransom-note/
#别人两行代码就能实现，用collections.counter
def canConstruct(ransomNote, magazine):
    i = 0
    while 1 :
        if ransomNote[i] in magazine :
            if ransomNote[0:i+1] in magazine :
                i = i + 1
            else :
                listransom = ransomNote.split(ransomNote[0:1+1],1) 
                listmagazine = magazine.split(ransomNote[0:1+1],1)
                i = 0
                ransomNote = listransom[0] + listransom[1]
                magazine = listmagazine[0] + listmagazine[1]
                continue
            if ransomNote == '':
                return True
        else :
            return False
            