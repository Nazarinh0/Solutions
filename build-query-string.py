def build_query_string(source):
    result = ''
    for k, v in sorted(source.items()):
        result = result + k + '=' + str(v)
        result += '&'
    return result[:-1]


print(build_query_string({'per': 10, 'page': 1}))