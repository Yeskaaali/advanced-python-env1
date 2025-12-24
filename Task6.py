a = int(input("First number: "))
operation = input("Operation: ")
b = int(input("Second number: "))
if operation == "+":
    result = a + b
if operation == "-":
    result = a - b
if operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
print(f"{a} {operation} {b} = {result}")