a = int(input())
sum = 0

for i in range(1, a+1, 1):
    if a % i == 0 and i != a:
        sum += i


if sum == a:
    print('P')
else:
    print('N')  