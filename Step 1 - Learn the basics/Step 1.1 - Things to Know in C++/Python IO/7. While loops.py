# While loop
# n = 10
# while n:
#     print(n, end=' ')
#     n-=1
# 10 9 8 7 6 5 4 3 2 1

# https://practice.geeksforgeeks.org/problems/while-loop-printtable/1

# Input: n = 1
# Output: 10 9 8 7 6 5 4 3 2 1

# Input: n = 2
# Output: 20 18 16 14 12 10 8 6 4 2


def printTable(n):
    multiplier = 10
    while multiplier>0:
        print(multiplier*n, end=' ')
        multiplier-=1
printTable(5)