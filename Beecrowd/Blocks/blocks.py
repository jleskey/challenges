import fileinput

test_file = fileinput.input()

t = int(test_file.readline().strip())

# For each test case
for case in range(1, t + 1):
    n = int(test_file.readline().strip())

    score = 0

    if n > 0:
        stack = [test_file.readline().strip().split(' ')[0:n]]

        while len(stack) > 0:
            #print("Stack:", stack)
            section = stack.pop()
            #print("Section:", section)

            if len(section) > 0:

                color_count = {}

                for color in section:
                    color_count.setdefault(color, 0)
                    color_count[color] += 1

                biggest_count = max(color_count.values())
                focal_color = None

                for color, count in color_count.items():
                    if count == biggest_count:
                        focal_color = color
                        break

                #print("Focal color:", focal_color, "@", biggest_count)

                segment_length = 0
                last_color = None
                focal_color_segments = 0
                remainder_sections = [[]]

                for color in section:
                    if color == focal_color:
                        if last_color != focal_color:
                            focal_color_segments += 1
                            if focal_color_segments % 2 == 0:
                                # Flush the remainder. This section would be played
                                # first and thus must be separate.
                                #print("Flushed remainder:", remainder_sections[-1])
                                stack.append(remainder_sections.pop())
                                remainder_sections.append([])
                        segment_length += 1
                    else:
                        if len(remainder_sections) == 0 or (last_color == focal_color and len(remainder_sections[0]) > 0):
                            # Start a new remainder section. This might be an
                            # inner section.
                            remainder_sections.append([])
                        remainder_sections[-1].append(color)
                    #print("Remainder sections:", remainder_sections)
                    last_color = color

                combined_remainder = []
                for section in remainder_sections:
                    combined_remainder.extend(section)
                #print("Combined remainder", combined_remainder)
                stack.append(combined_remainder)

                #print("Adding to score:", segment_length ** 2)
                score += segment_length ** 2


    print(f'Case {case}: {score}')
