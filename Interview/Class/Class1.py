class PowerGenerator:
    def __init__(self, max_exp):
        self.max_exp = max_exp

    def __iter__(self):
        self.exp = 0
        return self

    def __next__(self):
        if self.exp <= self.max_exp:
            result = 2 ** self.exp
            self.exp += 1
            return result
        else:
            raise StopIteration

try:
    gen = PowerGenerator(5)
    powers = [val for val in gen]
    print(powers)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Power generation complete.")