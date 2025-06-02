class Boom:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

cancel = input().split()
x = Boom(cancel[0], cancel[1], cancel[2])

print(f'code : {x.code}')
print(f'color : {x.color}')
print(f'second : {x.sec}')