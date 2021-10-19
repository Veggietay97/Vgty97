#!/usr/bin/python

"""
Python Functions and Recursions
"""
"""
QUESTION 1: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
["((()))","(()())","(())()","()(())","()()()"]
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
"""
def generateParenthesis(n):
    left = n
    right = n
    temp = []
    result = []
    getParenthesis(left, right, temp, result)
    return result

def getParenthesis(left, right, temp, result):
    if(left == 0 and right == 0):
        temp2 = ''.join(temp)
        result.append(temp2)
        temp.clear()
        temp2.strip()
        return result
    if(left > 0):
        getParenthesis(left-1, right, temp+['('], result)
    if(right > left):
        getParenthesis(left, right-1, temp+[')'], result)
    
    return result




"""
QUESTION 2: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
=========================================
Input: "race a car"
Output: false
Write a function named isPalindrome that takes a string as an input and returns a bool as an output.
"""

def isPalindrome(word):
	newword = ''.join(e for e in word if e.isalnum())
	newerword = newword.lower()
	return newerword == newerword[::-1]