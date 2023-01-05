# https://bit.ly/3w3qhDh

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
