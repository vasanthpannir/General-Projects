from collections import Counter

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'b': 150, 'c': 100, 'd': 50}

collected_dict = dict(Counter(dict1)+Counter(dict2))
print(collected_dict)
