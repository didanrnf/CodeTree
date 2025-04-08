a, b = map(int, input().split())
sum = 0

for i in range(min(a, b), max(a, b)+1):
    if i % 5 ==0:
        sum += i

print(sum)