'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718712/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_13

Input: 5

Output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

'''

n = 5
count = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        count+=1
        print(count, end=' ')
    print()