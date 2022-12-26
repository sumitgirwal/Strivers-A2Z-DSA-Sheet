# https://practice.geeksforgeeks.org/problems/triangle-number-1661428795/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_4

# Input: 5

# Output:
# 1
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5


n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(str(i),  end=' ')
    print()