def do_sort(L):
    J = []
    for i in range(len(L)):
        J.append(L[i])
    sorted(J,key = str.lower)
    return J

if __name__ == '__main__':
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    K = do_sort(L)
    print(K)