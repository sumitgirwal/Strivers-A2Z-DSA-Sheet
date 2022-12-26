'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285911/1/?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_17

Input: 4
Output:
   A
  ABA
 ABCBA
ABCDCBA
'''

n = 4
for i in range(1, n+1):
    print(' '*(n-i), end='')
    count = ord('A')
    for j in range(1, i+1):
        print(chr(count), end='')
        count+=1
    
    count-=2
    for j in reversed(range(i-1)):
        print(chr(count), end='')
        count-=1
    print()
