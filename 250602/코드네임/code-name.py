class Students:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
x=[]
for i in range(5):
    name, score = tuple(input().split())
    x.append(Students(name, int(score)))

min_score = 100
min_stu = ''
for j in range(5):
    if x[j].score < min_score:
        min_score = x[j].score
        min_stu = x[j].name

print(min_stu, min_score)