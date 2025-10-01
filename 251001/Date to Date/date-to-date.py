m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sum_month = 0

n1 = d1 - 1
n2 = num_of_days[m2] - d2
n3 = num_of_days[m1:m2+1]

for i in n3:
    sum_month += i

result = sum_month - n1 - n2
print(result)