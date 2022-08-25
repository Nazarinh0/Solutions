def reverse(num):
    """Reverse the given number"""
    
    tmp = str(abs(num))
    result = int(tmp[::-1])
    if num < 0:
        result *= -1
    if result in range(-2 ** 31, 2 ** 31 - 1):
        return result
    else:
        return 0

print(reverse(123))
