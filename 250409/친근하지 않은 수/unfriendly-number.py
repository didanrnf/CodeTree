a = int(input())
sum = 0
for i in range(1, a+1):
    if i % 2 == 0:
        continue
    elif i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue
    sum += 1
print(sum)   