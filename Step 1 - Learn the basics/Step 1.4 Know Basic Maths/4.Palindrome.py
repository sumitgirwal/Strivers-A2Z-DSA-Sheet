'''
https://practice.geeksforgeeks.org/problems/palindrome0746/1

Input: n = 55555
Output: Yes

class Solution
{
	public:
		string is_palindrome(int n)
		{
		    int temp = n;
		    int newD = 0;
		    while(n!=0){
		        int d = n%10;
		        newD = (newD*10) + d;
		        n=n/10;
		    }
		    
		    if(temp==newD){
		        return "Yes";
		    }
		    return "No";
		}
};

def is_palindrome(self, n):
		n = str(n)
		return "Yes" if n==n[::-1] else "No"
'''


def is_palindrome(self, n):
    n = str(n)
    return "Yes" if n==n[::-1] else "No"

 
