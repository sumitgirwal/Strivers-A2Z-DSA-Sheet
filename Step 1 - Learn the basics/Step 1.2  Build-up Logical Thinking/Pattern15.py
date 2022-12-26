'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285196/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_15
Input: 5

Output:
ABCDE
ABCD
ABC
AB
A
'''

n = 5
for i in reversed(range(1, n+1)):
    count = ord('A')
    for j in range(1, i+1):
        print(chr(count), end='')
        count+=1
    print()