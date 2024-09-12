nested_dict = {x: {y: y ** 2 for y in range(1, 4)} for x in range(1, 4)}
result = {x: {y: y ** 2 for y in range(1, 4)} for x in range(1, 4)}
print(result)
