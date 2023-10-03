import fileinput

stan = 0
ollie = 0
zero = 0

count = 0

for line in fileinput.input():
    numbers = list(map(int, line.split()))
    if count == 0:
        if stan > 0 or ollie > 0 or zero > 0:
            print(stan, ollie)
        count = numbers[0]
        stan = 0
        ollie = 0
    else:
        x = numbers[0]
        y = numbers[1]
        if (x > 0 and y > 0) or (x < 0 and y < 0):
            stan += 1
        elif (x > 0 and y < 0) or (x < 0 and y > 0):
            ollie += 1
        else:
            zero += 1

        count -= 1
    if line == '0\n':
        break