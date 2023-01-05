# https://bit.ly/3w2G4T5

int isPalindrome(string s)
	{
	    
	    int start = 0;
	    int end = s.length()-1;
	    while(start<=end){
	        if(s[start]!=s[end]){
	            return 0;        
	        }
	        start++;
	        end--;
	    }
	    
	    return 1;
	    
	}
