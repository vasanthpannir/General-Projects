nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result = [item for sub_list in nested_list for item in sub_list]
print(result)

