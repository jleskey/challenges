from fileinput import input

for line in input():
    if line == '*\n':
        break
    else:
        first_letters = {word[0].lower() for word in line.split()}
        print('Y' if len(first_letters) == 1 else 'N')
