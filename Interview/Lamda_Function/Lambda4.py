def make_multiplier(n):
    return lambda x: x * n

doubler = make_multiplier(2)
print(doubler(5))