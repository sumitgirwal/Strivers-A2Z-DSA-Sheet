'''

https://practice.geeksforgeeks.org/problems/pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_9

 
    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''

n = 5
for i in range(1, n+1):
    space=' '
    print(space*(n-i), end='')
    print('* '*(i), end='') 
    print()

for i in reversed(range(1, n+1)):
    space=' '
    print(space*(n-i), end='')
    print('* '*(i), end='') 
    print()