import fileinput

file = fileinput.input()

test_case_count = int(file.readline().strip())

for _ in range(test_case_count):
    n, m, l = map(int, file.readline().split())

    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    stack = []

    for _ in range(m):
        x, y = map(int, file.readline().split())
        matrix[x][y] = 1

    for _ in range(l):
        z = int(file.readline().strip())
        stack.append(z)

    total = 0

    while len(stack) > 0:
        total += 1
        for i, has_edge in enumerate(matrix[stack.pop()]):
            if has_edge:
                stack.append(i)

    print(total)
