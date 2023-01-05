# https://practice.geeksforgeeks.org/problems/bubble-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bubble-sort
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, lst, n):
         
        for i in range(n):
            for j in range(n-1):
                if lst[j]>lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst