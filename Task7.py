a = int(input("First number: "))
operation = input("Operation: ")
b = int(input("Second number: "))

if operation == "+":
    result = a + b
if operation == "-":
  result = a - b 
if operation == "*":
    result = a * b
if operation == "/":
    if b == 0:
        result = "Error: division by zero"
    else:
        result = a / b
else:
    result = "Unknown operation"
print(f"{a} {operation} {b} = {result}")