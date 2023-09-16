def raise_custom_value_error():
    raise ValueError("This is a custom ValueError.")

try:
    raise_custom_value_error()
except ValueError as e:
    print(f"ValueError: {e}")
