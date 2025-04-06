a, b = map(int, input().split())

n = a // b
m = a % b

x = []
for _ in range(20):
    m *= 10
    x.append(m//b)
    m = m % b

print(f'{str(n)}.{"".join(map(str, x))}')