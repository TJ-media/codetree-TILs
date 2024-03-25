a, b = map(int, input().split())

def sosu(c):
    if c == 1:
        return False
    for i in range(2, c):
        if c % i == 0:
            return False
        else:
            continue
    return True

def sumab(a,b):
    sum1 = 0
    for j in range(a, b+1):
        if sosu(j) == True:
            sum1 = sum1 + j
        else:
            continue
    return sum1

print(sumab(a,b))