# https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-1-to-n-without-using-loops
#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    //Complete this function
    void printNos(int n)
    {
        if(n==0){
          return;  
        } 
        printNos(n-1);
        cout<<(n)<<" ";
            
    }
};

https://bit.ly/3y2BiWz