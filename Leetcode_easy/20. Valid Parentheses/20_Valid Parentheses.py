#https://leetcode.com/problems/valid-parentheses/
#只要利用好dict，从头开始检索，开始一定是左侧的([{，所以当检索到第一个反向的括号，例如)]}的时候
#这个时候相当于找到了这段符号序列的中心，然后回头从从dict里找对应的value，按顺序排好，看与中线后面的是否相同就行了。
#例如({[ ..中线..]})中线左侧和右侧顺序正好是相反的，也就是关于中线对称。
def isValid(s):
    dic = {'{':'}','[':']','(':')'}
    L = []
    n = 1
    for i in s :
        if dic.__contains__(i):
            L.append(dic[i])
        else :
            if i == L[len(L)-n] :
                n = n + 1
                if n > len(L):
                    print('true')
                continue
            else :
                print('false')            
                break
isValid('{{{{{[[[[[]]]]]}}}}}')
    
