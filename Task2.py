x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
if x >= y and x >= z:
    max_salary = x
elif y >= z:
    max_salary = y
else:
    max_salary = z
if x <= y and x <= z:
    min_salary = x
elif y <= z:
    min_salary = y
else:
    min_salary = z
print(max_salary - min_salary)