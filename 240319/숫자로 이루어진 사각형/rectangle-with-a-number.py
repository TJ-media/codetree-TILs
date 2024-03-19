N = int(input())

a = 1

for i in range(N):
    for j in range(N):
        print(a, end = ' ')
        if a == 9:
            a = 1
        else:
            a = a+1
    print()