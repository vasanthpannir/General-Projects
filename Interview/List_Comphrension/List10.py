Example_Input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [[e[i] for e in Example_Input] for i in range(len(Example_Input[0]))]
print(result)