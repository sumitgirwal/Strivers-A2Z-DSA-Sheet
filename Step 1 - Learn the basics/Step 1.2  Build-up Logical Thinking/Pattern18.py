'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1662286302/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_18
Input: 5

Output:
E
E D
E D C
E D C B
E D C B A
'''

n = 5
for i in range(1, n+1):
    count = ord('A')+(n-1)
    for j in range(1, i+1):
        print(chr(count), end=' ')
        count-=1
    print()
    



