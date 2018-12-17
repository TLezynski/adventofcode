
def checkSum(fileName):
    file = open(fileName)
    lst = []
    for line in file:
        lst.append(line.strip())

    twice = 0
    thrice = 0
    for i in lst:
        counted_twice = False
        counted_thrice = False
        d = {}
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
        for k in d:
            if d[k] == 2 and not counted_twice:
                counted_twice = True
                twice += 1
            elif d[k] == 3 and not counted_thrice:
                counted_thrice = True
                thrice += 1

    return twice * thrice

print(checkSum("test.txt"))

print(checkSum("input.txt"))