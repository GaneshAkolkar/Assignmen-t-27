try:
    x = 5 / 2
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
else:
    print("Division successful.")
