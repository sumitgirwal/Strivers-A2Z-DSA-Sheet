# https://bit.ly/3SRqzXU

# https://practice.geeksforgeeks.org/problems/reverse-a-string/1

string reverseWord(string str){
  int start = 0;
  int end = str.length()-1;
  while(start<=end){
      swap(str[start], str[end]);
      start++;
      end--;
  }
  return str;
}