'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285334/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_16

Input: 5

Output:
A
BB
CCC
DDDD
EEEEE


'''

n = 5
count = ord('A')
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(count), end='')
    count+=1
    print()