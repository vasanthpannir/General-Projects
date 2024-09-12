numbers = list(range(-11, -1))
if len(numbers) < 2:
    raise ValueError("List must contain at least two unique numbers.")

highest_number = second_largest = float('-inf')

for number in numbers:
    if number > highest_number:
        second_largest = highest_number
        highest_number = number
    elif second_largest < number < highest_number:
        second_largest = number

print(second_largest)