a = int(input())
sum = 1
for i in range(1, 11, 1):
    sum *= i
    if sum >= a:
        print(i)
        break