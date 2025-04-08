sum = 0
cnt = 0
for i in range(10):
    a = int(input())
    if 0 <= a <= 200:
        sum += a
        cnt += 1
print(f'{sum} {sum/cnt:.1f}')