# Given N, find the number of ways to express N as a sum of 1, 3, 4
# ex: N = 4 , so number of ways to get 4 is : [4][1,3][3,1][1,1,1,1]
#ex N=5 so 6 ways: [4,1][1,4][1,3,1][3,1,1][1,1,3][1,1,1,1,1]
# can this problem be divided into smaller subproblem?
# f(5) = f(4) + 1 and F(5) = f(2) + 3 and f(1) + 4
#  

def numberfactor(n):
    if n in [0,1,2]:
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numberfactor(n-1)
        subP2 = numberfactor(n-3)
        subP3 = numberfactor(n-4)
    return subP1 + subP2 + subP3

print(numberfactor(6))