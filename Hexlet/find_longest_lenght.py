def find_longest_length(string):
    substring = ''
    
    if len(string) < 1:
        return 0
    
    for char in string:
        if char not in substring:
            substring += char
        else:
            substring = substring + ' ' + substring[substring.index(char)+1:] + char
    string_list = substring.split()
    print(max(string_list, key=len))
    return len(max(string_list, key=len))

print(find_longest_length('jabjcdel'))
