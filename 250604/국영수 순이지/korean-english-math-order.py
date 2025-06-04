class Student:
    def __init__(self, name, gook, eng, math):
        self.name = name
        self.gook = gook
        self.eng = eng
        self.math = math

n = int(input())
students = []
for _ in range(n):
    name, gook, eng, math = input().split()
    a = Student(name, int(gook), int(eng), int(math))
    students.append(a)

students.sort(key = lambda x : (-x.gook, -x.eng, -x.math))

for i in range(len(students)):
    print(students[i].name, students[i].gook, students[i].eng, students[i].math)