input_str = "Hello World"
result = ""
last_item = len(input_str)-1
for _ in range(0,len(input_str)):
    result += input_str[last_item]
    last_item-=1
print("".join(result))

