class Weather:
    def __init__(self, date, yoil, weather):
        self.date = date
        self.yoil = yoil
        self.weather = weather

    def __lt__(self, other):
        if (self.date).split('-')[0] == (other.date).split('-')[0]:
            if (self.date).split('-')[1] == (other.date).split('-')[1]:
                return (self.date).split('-')[2] < (other.date).split('-')[2]
            return (self.date).split('-')[1] < (other.date).split('-')[1]
        return (self.date).split('-')[0] < (other.date).split('-')[0]

n = int(input())
dayday = []
for _ in range(n):
    date, yoil, weather = input().split()
    a = Weather(date, yoil, weather)
    dayday.append(a)

is_rain = []
for i in range(len(dayday)):
    if dayday[i].weather == 'Rain':
        is_rain.append(dayday[i])

r = min(is_rain)
print(r.date, r.yoil, r.weather)