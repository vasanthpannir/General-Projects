numbers = list(range(1,11))
try:
    square_root = {x:(lambda y:y**0.5 if y>=0 else "invalid")(x) for x in numbers}
    print(square_root)
except Exception as e:
    print(f"error:{e}")
finally:
    print("The list if square roots are follows")

