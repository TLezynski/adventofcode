def readFromFile(fileName):
    file = open(fileName)
    lst = []
    for line in file:
        lst.append(line.strip())
    return lst


# PART 1:
def checkSum(fileName):
    lst = readFromFile(fileName)

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
# print(checkSum("test.txt"))
# print(checkSum("input.txt"))


# Part 2:

def checkString(stringA, stringB):
    unMatchingIndex = 0
    if stringA == stringB or len(stringA) != len(stringB):
        return False, unMatchingIndex

    numMatching = 0
    for i in range(0, len(stringA)):
        if stringA[i] == stringB[i]:
            numMatching += 1
        else:
            unMatchingIndex = i
    if numMatching == len(stringA) - 1:
        return True, unMatchingIndex
    return False, unMatchingIndex

def matchIDs(fileName):
    lst = readFromFile(fileName)
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            checked, strIDX = checkString(lst[i], lst[j])
            if checked:
                s = lst[i]
                sA = s[0:strIDX]
                sB = s[strIDX + 1:]
                return sA + sB


print(matchIDs("input.txt"))

