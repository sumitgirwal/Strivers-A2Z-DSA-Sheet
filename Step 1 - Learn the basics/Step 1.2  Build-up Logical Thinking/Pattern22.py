# https://practice.geeksforgeeks.org/problems/square-pattern-1662666141/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_22
''' 
Input: 4
Output:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''
n = 4
size = 2*n-1
arr = [[0]*size for i in range(size)]
start = 0
end = size-1
while n!=0:
    for i in range(start, end+1):
        for j in range(start, end+1):
            if i==start or i==end or j==start or j==end:
                arr[i][j] = n
    start+=1
    end-=1
    n-=1

# Printing pattern
for i in arr:
    for j in i:
        print(j, end=' ')
    print()