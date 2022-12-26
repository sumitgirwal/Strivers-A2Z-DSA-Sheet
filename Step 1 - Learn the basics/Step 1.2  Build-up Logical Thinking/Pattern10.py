'''

https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718013/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_10

Input: 5

Output:
* 
* * 
* * * 
* * * * 
* * * * *
* * * *
* * *
* *
*

'''

n = 5
for i in range(1, n+1):
    print('* '*(i), end='') 
    print()

for i in reversed(range(1, n)):
    print('* '*(i), end='') 
    print()