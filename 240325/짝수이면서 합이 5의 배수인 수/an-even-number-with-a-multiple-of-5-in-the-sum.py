n = int(input())

def yesoryes(n):
    if n % 2 == 0:
        if (n//10 + n%10) % 5 == 0:
            return "Yes"
        else:
            return "No"
    else:
        return "No"

print(yesoryes(n))