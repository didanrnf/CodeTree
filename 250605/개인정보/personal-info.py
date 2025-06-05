class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
people = []
for _ in range(5):
    name, height, weight = input().split()
    people.append(Person(name, int(height), float(weight)))

def print_list(x):
    for i in range(5):
        print(x[i].name, x[i].height, x[i].weight)

people.sort(key = lambda x : (x.name))
print("name")
print_list(people)
print()
people.sort(key = lambda x : (-x.height))
print("height")
print_list(people)