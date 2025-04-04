a, b, c = map(int, input().split())

min_num = 0

if a < b and a < c:
    min_num = a
elif b < a and b < c:
    min_num = b
else:
    min_num = c

print(min_num)