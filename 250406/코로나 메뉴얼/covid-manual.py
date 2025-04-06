a, a1 = input().split()
b, b1 = input().split()
c, c1 = input().split()
a1 = int(a1)
b1 = int(b1)
c1 = int(c1)
emer = 0

if a == 'Y' and a1 >= 37:
    emer += 1

if b == 'Y' and b1 >= 37:
    emer += 1

if c == 'Y' and c1 >= 37:
    emer += 1

if emer >= 2:
    print('E')
else:
    print('N')