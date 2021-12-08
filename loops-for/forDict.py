def reverse_dict(dict):
    lo = {}
    for k,v in dict.items():
        lo[v] = k
    return lo
dict = {'first': 'первый', 'second': 'второй'}
print(reverse_dict(dict))