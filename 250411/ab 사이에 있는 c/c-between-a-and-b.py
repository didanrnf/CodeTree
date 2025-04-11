a, b, c = map(int, input().split())
q = False
for i in range(a, b+1):
    if i % c == 0:
        q = True
    else:
        pass

if q == True:
    print('YES')
else:
    print('NO')