class product:
    def __init__(self, name = '', code = 0):
        self.n = name
        self.c = code

x = product('codetree', 50)
print(f'product {x.c} is {x.n}')

a = input().split()
x = product(a[0], int(a[1]))
print(f'product {x.c} is {x.n}')