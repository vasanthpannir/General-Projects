input_list = [1, 2, 3, 2, 4, 3, 5, 1, 6]
duplicate = []
for e in input_list:
    if e not in duplicate:
        duplicate.append(e)
print(duplicate)
