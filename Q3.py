try:
    x = 5 / 0
except ArithmeticError as e:
    print(f"ArithmeticError: {e}")
