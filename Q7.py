try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
finally:
    print("This code will always execute.")
