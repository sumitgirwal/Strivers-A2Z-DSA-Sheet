'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1662284916/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_14

Input: 5

Output:
A
AB
ABC
ABCD
ABCDE

'''

n = 5
for i in range(1, n+1):
    count = ord('A')
    for j in range(1, i+1):
        print(chr(count), end='')
        count+=1
    print()