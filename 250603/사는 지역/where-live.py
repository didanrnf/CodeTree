class Person:
    def __init__(self, name, bunzi, ziyeok):
        self.name = name
        self.bunzi = bunzi
        self.ziyeok = ziyeok

    def __lt__(self, other):
        return self.name < other.name

n = int(input())
x = []
for _ in range(n):
    name, bunzi, ziyeok = input().split()
    people = Person(name, bunzi, ziyeok)
    x.append(people)

latest = max(x)
print(f'name {latest.name}')
print(f'addr {latest.bunzi}')
print(f'city {latest.ziyeok}')