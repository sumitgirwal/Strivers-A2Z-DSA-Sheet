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
        return f"{a} {b}"
    return gcd(b, a%b)


print(gcd(5, 10))
print(gcd(10, 5))