'''
https://practice.geeksforgeeks.org/problems/double-triangle-pattern-1662664259/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_12
Input: 5

Output:
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1
'''

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    for j in range(1, n-i+1):
        print(' ', end=' ')
    for j in range(1, n-i+1):
        print(' ', end=' ')
    for j in reversed(range(1, i+1)):
        print(j, end=' ')
    print()