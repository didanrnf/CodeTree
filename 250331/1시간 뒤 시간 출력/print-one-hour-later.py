h, m = map(int, input().split(":"))
h += m // 60
m %= 60


if h >= 24:
    h %= 24

print(f'{h+1}:{m}')