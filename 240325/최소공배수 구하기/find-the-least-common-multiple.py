a,b = map(int,input().split())

def gcd(a,b):
    while a*b != 0:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a + b

print(int(a*b/gcd(a,b)))