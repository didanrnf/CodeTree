a, b = map(int, input().split())

if a > b:
    for i in range(a, b-1, -1):
        print(i, end = ' ')
if b > a:
    for i in range(b, a-1, -1):
        print(i, end = ' ')