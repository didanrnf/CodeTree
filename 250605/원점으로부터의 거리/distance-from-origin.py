class Street:
    def __init__(self, x1, x2, number):
        self.x1 = x1
        self.x2 = x2
        self.number = number

p = []
y1 = 0
y2 = 0

n = int(input())
for i in range(n):
    i = int(i)+1
    x1, x2 = map(int, input().split())
    p.append(Street(x1, x2, i))

p.sort(key = lambda x : abs(x.x1 - y1) + abs(x.x2 - y2))

for j in range(n):
    print(p[j].number)