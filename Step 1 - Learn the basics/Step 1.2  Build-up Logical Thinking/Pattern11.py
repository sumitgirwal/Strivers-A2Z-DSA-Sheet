'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718455/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_11

Input: 5

Output:
1 
0 1 
1 0 1
0 1 0 1 
1 0 1 0 1

'''

n = 5
for i in range(1, n+1):
    start=(i%2)
    for j in range(i):
        print(start, end=' ')
        start = 0 if start==1 else 1
    print()

        
     
