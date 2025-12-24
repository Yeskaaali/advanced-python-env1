a = int(input())
if a >= 1:
    total = 0
    for i in range(1, a + 1):
        total += i
    print(total)
else:
    total = 0
    for i in range(a, 2):
        total += i
    print(total)