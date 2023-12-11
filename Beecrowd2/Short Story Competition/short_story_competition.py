from fileinput import input

stdin = input()

while True:
    line1 = stdin.readline()
    if not line1:
        break
    line2 = stdin.readline()

    word_count, max_lines_per_page, max_chars_per_line = map(int, line1.split())
    words = line2.split()
    words.reverse()

    pages = 1

    chars_in_line = 0
    lines_in_page = 1

    while len(words) > 0:
        word = words.pop()
        chars = len(word) + (0 if chars_in_line == 0 else 1)

        if chars_in_line + chars > max_chars_per_line:
            lines_in_page += 1
            chars_in_line = chars - 1
        else:
            chars_in_line += chars

        if lines_in_page > max_lines_per_page:
            pages += 1
            lines_in_page = 1

    print(pages)
