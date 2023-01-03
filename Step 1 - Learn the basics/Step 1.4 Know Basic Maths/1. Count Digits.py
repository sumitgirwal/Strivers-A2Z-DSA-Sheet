'''
https://practice.geeksforgeeks.org/problems/count-digits5716/1
Input:
N = 12
Output:
2
Explanation:
1, 2 both divide 12 evenly

Input:
N = 23
Output
0
Explanation:
2 and 3, none of them
divide 23 evenly

'''
class Solution:
    def evenlyDivides (self, n):
        count = 0
        temp = n
        while n:
            d = n%10
            if d!=0:
                if temp%d==0:
                    count+=1
            n//=10
        return count



