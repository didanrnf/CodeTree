a, b, c = map(int, input().split())

# Please write your code here.
day = a - 11
hour = b - 11
minutes = c -11


if minutes < 0:
    minutes += 60
    hour -= 1

if hour < 0:
    hour += 24
    day -= 1
  
sum_minutes = day*24*60 + hour*60 + minutes

if a <= 11 and b <= 11 or c < 11:
    sum_minutes = -1

print(sum_minutes)