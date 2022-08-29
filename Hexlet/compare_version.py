def compare_version(x, y):
    minor_x = x.split('.')[1]
    minor_y = y.split('.')[1]
    major_x = x.split('.')[0]
    major_y = y.split('.')[0]
    if (int(major_x), int(minor_x)) < (int(major_y), int(minor_y)):
        return -1
    if (int(major_x), int(minor_x)) > (int(major_y), int(minor_y)):
        return 1
    if (int(major_x), int(minor_x)) == (int(major_y), int(minor_y)):
        return 0


print(compare_version('0.2', '0.12'))
