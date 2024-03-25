a, b = map(int, input().split())

def digits_to_list(number):
    return [int(digit) for digit in str(number)]

def three(a,b):
    count = 0
    for i in range(a, b+1):
        if i % 3 == 0:
            count = count + 1
        else:
            if 3 in digits_to_list(i) or 6 in digits_to_list(i) or 9 in digits_to_list(i):
                count = count + 1
            else:
                continue
    return count

print(three(a,b))