#Expanding around each index treating them as center. so time complexity - n*n
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlength=1
        start=0
        for i in range(1,len(s)):
            low=i-1
            high=i
            while(low>=0 and high<len(s) and s[low]==s[high]):
                if(high-low+1>maxlength):
                    start=low
                    maxlength=high-low+1
                low=low-1
                high=high+1
            low=i-1
            high=i+1
            while(low>=0 and high<len(s) and s[low]==s[high]):
                if(high-low+1>maxlength):
                    start=low
                    maxlength=high-low+1
                low=low-1
                high=high+1
        return s[start:start+maxlength]
      
 #the above can be modified in linear time using Manacher.
#Manacher rules
#1. Do not pick a character as center if the palindrome around it is totally contained under current palindrome.
#2. Pick a character if the palindrome around it expands till the right edge of current palindrome and its mirror is perfect prefix.
#3. Do not Pick a character if the palindrome around it expands till the right edge of current palindrome and its mirror is not a perfect prefix.
#4. End if the current palndroe reaches till end of the input
#Code reference link - https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-4/
