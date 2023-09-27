import fileinput

line = fileinput.input().readline()

word_list = line.split()

word_set = set(word_list)

if len(word_list) > len(word_set):
    print("no")
else:
    print("yes")