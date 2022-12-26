'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1661493231/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_8

Input: 5

Output:

*********
 *******
  *****
   ***
    *
'''
n = 5
for i in range(1, n+1):
    space=' '
    print(space*(i-1), end='')
    print('*'*(n-i+1), end='') 
    print('*'*(n-i), end='') 
    print()

