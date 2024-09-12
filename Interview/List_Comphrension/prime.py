Example_Input = [[3, 5, 6], [8, 10, 12], [15, 18, 20]]
result = [x for e in Example_Input for x in e if x % 2 == 1]
print(result)