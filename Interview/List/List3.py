numbers = [1, 2, 3, 4, 5, 6, 7, 8]
mid_element = len(numbers) // 2
first_half = []
second_half = []
for e in numbers:
    if e <= mid_element + 1:
        first_half.append(e)
    elif mid_element+1<=len(numbers):
        second_half.append(e)
result = second_half+first_half
print(result)