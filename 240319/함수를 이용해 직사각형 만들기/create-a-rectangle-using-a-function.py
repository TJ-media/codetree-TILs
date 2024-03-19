input_str = input()

values = list(map(int, input_str.split()))

n = values[0]
m = values[1]

for i in range(n):
    print('1'*m)