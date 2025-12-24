A = input()
b_part, c_part = A.split('.')
newnumber = int(c_part) + int(b_part) / 100
print(f"{newnumber:.2f}")