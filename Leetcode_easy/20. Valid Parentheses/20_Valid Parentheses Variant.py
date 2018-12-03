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
            P = 0
            L = 0
    for i in range(0,len(M)-1,2) :
        if M[i] == M[i+1]: 
            if i+2 == len(M):
                print('true')
            else :
                continue 
        else :
            print('false')
            break 