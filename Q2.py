def raise_value_error():
    raise ValueError("This is a custom ValueError.")

try:
    raise_value_error()
except ValueError as e:
    print(f"ValueError: {e}")
