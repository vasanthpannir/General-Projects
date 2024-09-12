list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = [(x,y) for x in list1 for y in list2]
print(result)