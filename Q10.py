try:
    try:
        x = 5 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
except Exception as e:
    print(f"Outer Exception: {e}")
