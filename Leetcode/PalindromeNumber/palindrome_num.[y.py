def isPalindrome(x):
    '''Check if the given number is palindrome'''
    if x < 0:
        return False
    else:
        string = str(x)
        return string == string[::-1]


print(isPalindrome(123))
