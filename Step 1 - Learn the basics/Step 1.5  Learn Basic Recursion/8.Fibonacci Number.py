# https://bit.ly/3QUkkk2
 


class Solution
{
    public:
    //Function to return list containing first n fibonacci numbers.
    vector<long long> printFibb(int n) 
    {
        vector<long long> v;
        long long first=0, second=1, ans;
        if(n>=1){
            v.push_back(second);
        }
        for(int i=1; i<n; i++){
            ans = first+second;
            first = second;
            second = ans;
            v.push_back(ans);
        }
        return v;
       
    }
};