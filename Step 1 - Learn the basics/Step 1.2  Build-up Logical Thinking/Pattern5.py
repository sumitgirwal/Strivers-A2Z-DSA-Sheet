# https://practice.geeksforgeeks.org/problems/triangle-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_5

# Input: 5

# Output:
# * * * * *
# * * * * 
# * * * 
# * *  
# * 

n = int(input())
for i in range(0, n):
    for j in range(n-i):
        print('*', end=' ')
    print()