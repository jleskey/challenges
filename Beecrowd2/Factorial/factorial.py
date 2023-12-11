from fileinput import input

n = int(input().readline().strip())

factorial_cache = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]

balance = n
k = 0

while balance > 0:
    selection = None
    for value in factorial_cache:
        if value > balance:
            break
        selection = value

    k += 1
    balance -= selection

print(k)
