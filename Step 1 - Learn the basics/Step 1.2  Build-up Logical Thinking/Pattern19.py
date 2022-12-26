'''
https://practice.geeksforgeeks.org/problems/double-triangle-pattern/1/?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_19
Input: 5
Output:
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''
n = 5
for i in range(1, n+1):
    print('*'*(n-i+1), end='')
    print(' '*(i-1), end='')
    print(' '*(i-1), end='')
    print('*'*(n-i+1), end=' ')
    print()

for i in reversed(range(1, n+1)):
    print('*'*(n-i+1), end='')
    print(' '*(i-1), end='')
    print(' '*(i-1), end='')
    print('*'*(n-i+1), end=' ')
    print()