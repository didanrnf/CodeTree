n = int(input())

# Please write your code here.
def asd(n):
    a = 1
    for i in range(n):
        for j in range(n):
            if a > 9:
                a = 1
            print(a, end = ' ')
            a += 1

        print()

asd(n)