original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result = {k: v for k, v in original_dict.items() if v % 2 == 0}
print(result)
