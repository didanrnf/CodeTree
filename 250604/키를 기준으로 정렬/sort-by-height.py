class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
students = []
for _ in range(n):
    name, height, weight = input().split()
    a = Student(name, height, weight)
    students.append(a)
    
students.sort(key = lambda x : x.height)

for i in range(len(students)):
    print(students[i].name, students[i].height, students[i].weight)