a = int(input())
sum = 0
for i in range(a):
    n = int(input())
    if n % 3 == 0 and n % 2 != 0:
        sum += n


print(sum)
