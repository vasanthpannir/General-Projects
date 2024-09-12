class Ndex:
    def finding_index(self, list1, req):
        try:
            # Enumerate through the list to get both index and value
            ind = enumerate(list1)
            for i, e in ind:
                if i == req:
                    print(f"Value at index {req}: {e}")
                    return  # Exit after finding the index
            # If no matching index is found, print invalid input
            print("Invalid Input")
        except IndexError:
            return "Invalid Input"

index = Ndex()
list1 = [10, 20, 30, 49, 50, 69]
try:
    req = int(input("Enter the index of the number you want from the list:\n"))
    if req >= len(list1) or req < 0:
        print("Input error: Index out of range")
    else:
        index.finding_index(list1, req)
except ValueError:
    print("Input error: Please enter a valid integer")
