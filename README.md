🔁 Valid Palindrome Checker

This program checks whether a given string is a valid palindrome.
A string is considered a palindrome if it reads the same forward and backward after ignoring:

  Non-alphanumeric characters
  
  Letter casing (uppercase vs lowercase)

📌 Problem Statement

Given a string s, return True if it is a palindrome, or False otherwise.

Only letters and digits are considered, and comparisons are case-insensitive.

🧠 Algorithm (Two-Pointer Technique)

The solution uses two pointers:

  left starts at the beginning of the string
  
  right starts at the end of the string

Steps:

  Skip non-alphanumeric characters from both ends
  
  Compare characters after converting to lowercase
  
  Move pointers inward
  
  If all characters match → palindrome
