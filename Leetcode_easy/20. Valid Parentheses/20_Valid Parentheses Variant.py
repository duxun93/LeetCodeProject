#if we have str like this :{[()]}{[]},{[(]}{[)]}
# how to deal?
def isValid(s):
    dic = {'{':'}','[':']','(':')'}
    L = []
    P = []
    M = []
    for i in s :
        if dic.__contains__(i):
            L.append(dic[i])
        else :
            P.append(i)
        if len(L) == len(P):
            M.append(L)
            M.append(P)
            P = []
            L = []
    for i in range(0,len(M)-1,2) :
        if M[i] == list(reversed(M[i+1])) : 
            if i+2 == len(M):
                print('true')
                break
            else :
                continue 
        else :
            print('false')
            break
#isValid('{[()]}{[]}') 
isValid('{[(]}{[)]}{[()]}{[]}')#这里有bug，还没修复。