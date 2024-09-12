my_dict = {'a': 5, 'b': 12, 'c': 18, 'd': 7}
result = [key for key,value in my_dict.items() if value>10]
print(result)

