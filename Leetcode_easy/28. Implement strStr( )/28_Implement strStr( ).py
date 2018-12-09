#https://leetcode.com/problems/implement-strstr/
#KMP算法。不过python可以用in来实现，只需要确定对应的位置就可以了。
def strStr(haystack, needle):
    if needle in haystack:
        j = 0
        for i in range(0,len(haystack)-1):
            if haystack[i] == needle[j]:
                j = j + 1
                if j == len(needle) :
                    return (i-j+1)
                    break
    else :
        return -1
print(strStr(haystack = "transformors", needle = "for"))
print(strStr(haystack = "aaaaaaa", needle = "abc"))