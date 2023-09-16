def raise_arithmetic_error():
    x = 5 / 0

try:
    raise_arithmetic_error()
except ArithmeticError as e:
    print(f"ArithmeticError: {e}")
