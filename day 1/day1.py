
def readFromFile(name):
    file = open(name)
    lst = []
    for line in file:
        line = line.rstrip()
        lst.append(line)
    return lst

def addToDict(n, d):
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

def main(name):
    lst = readFromFile(name)
    total = 0
    i = 0
    d = {}
    while(True):
        if(i >= len(lst)):
            i = 0
            continue
        if(lst[i][0] == "+"):
            total += int(lst[i][1:])
        elif(lst[i][0] == "-"):
            total -= int(lst[i][1:])
        addToDict(total, d)
        if(d[total] == 2):
            print("Frequency to reach twice is : ", total)
            break
        i += 1
    print("Input = ", lst, "\nResult = ", total)


main("input.txt")