'''
https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1
Input:
A = 5 , B = 10
Output:
10 5
Explanation:
LCM of 5 and 10 is 10, while
thier GCD is 5.
'''


def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    lcm = (a*b)//gcd(a,b)
    return lcm

a = 14
b = 8
print(gcd(a, b))
print(lcm(a, b))