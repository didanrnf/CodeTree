class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())

students = []
for i in range(n):
    i = int(i) + 1 
    height, weight = map(int, input().split())
    students.append(Student(height, weight, i))

students.sort(key = lambda x:(-x.height, -x.weight, x.number))

for j in range(n):
    print(students[j].height, students[j].weight, students[j].number)