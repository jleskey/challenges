import fileinput
import re

caseNum = 0
n = -1
m = -1
integers = []
sums = []

for line in fileinput.input():
    # Let's ignore non-integers.
    if re.search('^\-?\d+$', line):
        lineData = int(line)

        if n == 0 and m == 0:
            n = -1
            m = -1

        if n > 0:
            n -= 1
            integers.append(lineData)
        elif n == 0:
            if m > 0:
                m -= 1
                query = lineData
                sums.sort(key = lambda sum : abs(query - sum + 1))
                if (len(sums) > 0):
                    print(f'Closest sum to {query} is {sums[0]}.')
            else:
                m = lineData
                for i1, n1 in enumerate(integers):
                    for i2, n2 in enumerate(integers):
                        if i1 != i2:
                            sums.append(n1 + n2)
        else:
            caseNum += 1
            print(f'Case {caseNum}:')
            n = lineData
            integers.clear()
            sums.clear()