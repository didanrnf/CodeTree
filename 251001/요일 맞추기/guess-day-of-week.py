m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yo_of_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
sum_days1 = 0

for i in range(1, m1):
    sum_days1 += num_of_days[i]
sum_days1 += d1

sum_days2 = 0
for i in range(1, m2):
    sum_days2 += num_of_days[i]
sum_days2 += d2

result = sum_days2 - sum_days1 + 1
now_index = result % 7

yo = yo_of_days[now_index]
print(yo)