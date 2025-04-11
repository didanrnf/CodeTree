sum = 0
cnt = 0
while True:
    a = int(input())
    if a < 20 or a > 29:
        break
    else:
        sum += a
        cnt += 1

print(f'{sum / cnt:.2f}')
