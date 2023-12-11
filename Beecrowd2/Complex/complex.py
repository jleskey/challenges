from fileinput import input

stdin = input()

case_count = int(stdin.readline().strip())

for i in range(case_count):
    real, j = map(int, stdin.readline().split())

    if j == 0:
        print(1)
    elif real == 0:
        print(2)
    elif abs(j) != abs(real) or abs((complex(real, j)**4).real) > 2 ** 30:
        print("TOO COMPLICATED")
    else:
        print(4)
