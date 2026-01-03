#s:str means s as a string  -> type hinting 
def palindrome(s:str) -> bool: 
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

if __name__ == "__main__":
    test_string= "A man, a plan, a canal: Panama"
    result = palindrome(test_string)
    print(f'Is the string "{test_string}" a valid palindrome? {result}')