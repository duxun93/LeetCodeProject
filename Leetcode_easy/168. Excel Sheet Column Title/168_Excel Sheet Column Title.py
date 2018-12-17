#https://leetcode.com/problems/excel-sheet-column-title/
#巧用dict
def convertToTitle(n):
    dictnum = {1:'A',2:'B',
               3:'C',4:'D',
               5:'E',6:'F',
               7:'G',8:'H',
               9:'I',10:'J',
               11:'K',12:'L',
               13:'M',14:'N',
               15:'O',16:'P',
               17:'Q',18:'R',
               19:'S',20:'T',
               21:'U',22:'V',
               23:'W',24:'X',
               25:'Y',26:'Z'}
    a = n //26
    b = n % 26
    cons = a*'A' + dictnum[b]
    return cons
print(convertToTitle(128))
#为什么我觉得这道题就是这么简单，到底哪里错了呢？为什么网上都是用进制算的，这么麻烦的吗，
#明明一个dict就可以解决了呀