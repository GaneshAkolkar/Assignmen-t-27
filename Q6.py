def calculator(a, b, operator):
    try:
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        else:
            raise ValueError("Invalid operator")
        return result
    except (ValueError, ZeroDivisionError) as e:
        return f"Error: {e}"

result = calculator(10, 0, '/')
print(result)
