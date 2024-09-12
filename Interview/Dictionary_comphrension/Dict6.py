input_str = "python"
alst = {}
for e in input_str:
    if e in alst:
        alst[e] += 1
    else:
        alst[e] = 1
print(alst)
