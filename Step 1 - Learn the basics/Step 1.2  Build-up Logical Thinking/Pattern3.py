# https://practice.geeksforgeeks.org/problems/triangle-number/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_3
# 5

# 1
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(str(j),  end=' ')