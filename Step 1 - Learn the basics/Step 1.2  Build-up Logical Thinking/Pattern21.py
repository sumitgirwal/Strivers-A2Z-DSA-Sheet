'''
https://practice.geeksforgeeks.org/problems/square-pattern-1662287714/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_21
Input: 4
Output:
****
*  *
*  *
****
'''
n = 10
for i in range(1, n+1):
    if i==1 or i==n:
        print('*'*n, end='')
    else:
        print('*'+' '*(n-2)+'*', end='')
    print()


