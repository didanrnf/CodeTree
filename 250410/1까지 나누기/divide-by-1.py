a = int(input())
cnt = 0

for i in range(1, 5001):
    if (a // i) <= 1:
        break
    else:
        a //= i
        cnt += 1
print(cnt+1)