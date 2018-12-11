#https://leetcode.com/problems/length-of-last-word/
#it is easy for python.
#str.split( ),find the last word.
def lengthOfLastWord(s):
    strs = s.split(' ')[-1]
    length = len(strs)
    return length
print(lengthOfLastWord("Hello World"))    