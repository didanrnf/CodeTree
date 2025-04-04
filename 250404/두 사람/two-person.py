a, a1 = input().split()
b, b1 = input().split()

a = int(a)
b = int(b)

if (a >= 19 and a1 == 'M') or (b >= 19 and b1 == 'M'):
    print(1)
else:
    print(0)