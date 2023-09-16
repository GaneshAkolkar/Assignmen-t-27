try:
    x = 5 / 0
except (ArithmeticError, ZeroDivisionError) as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Other Exception: {e}")
