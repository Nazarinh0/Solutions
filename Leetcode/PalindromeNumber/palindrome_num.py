def is_palindrome(num):
    '''Checks if the given number is palindrome'''
    
    if num < 0:
        return False
    else:
        string = str(num)
        return string == string[::-1]


print(is_palindrome(123))
