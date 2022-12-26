# https://practice.geeksforgeeks.org/problems/triangle-number-1661489840/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_6

# Input: 5

# Output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2  
# 1 


n = int(input())
for i in range(0, n):
    for j in range(1, n-i+1):
        print(j, end=' ')
    print()

