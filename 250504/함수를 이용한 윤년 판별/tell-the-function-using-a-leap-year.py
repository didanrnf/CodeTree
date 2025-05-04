y = int(input())

# Please write your code here.
def is_yoon(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            return False
        return True
    

if is_yoon(y):
    print("true")
else:
    print("false")