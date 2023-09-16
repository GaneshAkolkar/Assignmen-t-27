try:
    int("invalid")
except ValueError as e:
    print(f"ValueError: {e}")
