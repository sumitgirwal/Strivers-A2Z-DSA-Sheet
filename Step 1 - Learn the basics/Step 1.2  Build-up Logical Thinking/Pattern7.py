# https://practice.geeksforgeeks.org/problems/triangle-pattern-1661492263/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_7

# Input: 5

# Output:
'''
    *
   ***  
  *****
 *******
*********
'''

n = 5
for i in range(1, n+1):
    space=' '
    print(space*(n-i), end='')
    print('*'*(i), end='') 
    print('*'*(i-1), end='') 
    print()






