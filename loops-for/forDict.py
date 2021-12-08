def reverse_dict(dict):
    lo = {}
    for k,v in dict.items():
        lo[v] = k
    return lo