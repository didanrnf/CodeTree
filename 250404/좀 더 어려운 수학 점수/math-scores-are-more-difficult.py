a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

if a1 > b1:
    print('A')
elif b1 > a1:
    print('B')

if a1 == b1:
    if a2 > b2:
        print('A')
    elif b2 > a2:
        print('B')