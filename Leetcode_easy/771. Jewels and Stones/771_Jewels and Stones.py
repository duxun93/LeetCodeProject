#https://leetcode.com/problems/jewels-and-stones/
def numJewelsInStones(S, J ):
    num = 0
    for i in S:
        for j in J :
            if i == j :
                num = num + 1
            else :
                continue
    return num
print(numJewelsInStones('Aa','AAaabbAbB')) 