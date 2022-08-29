def enlarge(image):
    result = []
    
    for item in image:
        char_list = list(item)
        i = 0
        if char_list == []:
            return image * 2
        for char in char_list:
            char_list[i] += char_list[i]
            enlarged_line = ''.join(char_list)
            i += 1
        result.extend([enlarged_line, enlarged_line])
    return result


frame = [
    '****',
    '*  *',
    '*  *',
    '****'
]
f = ['']
print(enlarge(f))
